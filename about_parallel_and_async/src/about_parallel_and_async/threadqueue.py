## References
#  - https://www.troyfawkes.com/learn-python-multithreading-queues-basics/
#  - https://superfastpython.com/thread-queue/
#  - https://medium.com/@surve.aasim/thread-synchronization-in-python-using-queue-1be0df535a66
#  - https://docs.python.org/3/library/threading.html
#
import csv
from datetime import datetime
import os
from pathlib import Path
from queue import Queue
from threading import Thread
import time

from pymssql import connect as sqlconnect, Warning as SqlWarning, Error as SqlError

SQL_HOSTNAME = os.getenv("AZURE2ZEUS_SQL_HOSTNAME")
SQL_DBNAME = os.getenv("AZURE2ZEUS_SQL_DBNAME")
SQL_USRNAME = os.getenv("AZURE2ZEUS_SQL_DBANAME")
SQL_USRPWD = os.getenv("AZURE2ZEUS_SQL_DBAPWD")

EXPECTED_TOTAL_ROWS = 29_764  # 6_109_152
Datafiles_path = Path(__file__).parent.joinpath("data")
if not Datafiles_path.exists():
    Datafiles_path.mkdir(parents=True, exist_ok=True)

slices = []
for y in range(2024, 2025):
    for w in range(1, 54):
        query = (
            "SELECT * FROM [jira_historical_issues_weekly_snapshot_maindataset_prod] "
            f"WHERE YEAR([hist_timestamp]) = {y} AND DATEPART(Week,[hist_timestamp]) = {w};"
        )
        slices.append((y, w, query))


def Retrieve_slice_query(in_queue: Queue, out_queue: Queue):
    while True:
        y, w, query_slice = in_queue.get()
        # print(
        #     f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] Getting {y}-{w:0>2} slice"
        # )
        start = time.perf_counter_ns()
        with sqlconnect(
            server=SQL_HOSTNAME,
            database=SQL_DBNAME,
            user=SQL_USRNAME,
            password=SQL_USRPWD,
            as_dict=False,
            autocommit=True,
        ) as sql_cnx:
            with sql_cnx.cursor() as slice_cursor:
                slice_cursor.execute(query_slice)
                r = slice_cursor.fetchall()
                headers = [h[0] for h in slice_cursor.description]

        if len(r):
            elapsed_ns = time.perf_counter_ns() - start
            out_queue.put((y, w, elapsed_ns, headers, r))
            print(
                f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] Retrieved {y}-{w:0>2}: "
                f"{len(r): >7,} rows in {elapsed_ns/1_000_000_000.0: >18,.6f} secs, "
                f"({len(r)/(elapsed_ns/1_000_000_000.0): >12,.6f} rows/sec)"
            )
        in_queue.task_done()


def Save_query_results(in_queue: Queue, out_queue: Queue, folder: Path):
    while True:
        y, w, slice_query_ns, headers, r = in_queue.get()
        filename = f"{y}-{w:0>2}.csv"
        filepath = f"{folder.joinpath(filename).resolve()}"
        start = time.perf_counter_ns()
        with open(filepath, "w", newline="") as csvfile:
            slicewriter = csv.writer(csvfile, dialect="excel")
            slicewriter.writerow(headers)
            slicewriter.writerows(r)
        elapsed_ns = time.perf_counter_ns() - start
        out_queue.put(
            {
                "year": y,
                "week_number": w,
                "slice_query_ns": slice_query_ns,
                "save_query_ns": elapsed_ns,
                "rows": len(r),
            }
        )
        print(
            f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] Saved     {y}-{w:0>2}: "
            f"{len(r): >7,} rows in {elapsed_ns/1_000_000_000.0: >18,.6f} secs, "
            f"({len(r)/(elapsed_ns/1_000_000_000.0): >12,.6f} rows/sec)"
        )

        in_queue.task_done()


results_queue = Queue(maxsize=0)

query_slice_queue = Queue(maxsize=0)
save_query_queue = Queue(maxsize=0)

num_cores = os.cpu_count()
max_threads = (num_cores * 8) // 10

for i in range(max_threads):
    wkr = Thread(
        target=Retrieve_slice_query,
        args=(query_slice_queue, save_query_queue),
        name=f"Retrieve_slice_query.{i:0>4}",
        daemon=True,
    )
    wkr.start()

for i in range(max_threads):
    wkr = Thread(
        target=Save_query_results,
        args=(save_query_queue, results_queue, Datafiles_path),
        name=f"Save_query_results.{i:0>4}",
        daemon=True,
    )
    wkr.start()

print(f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] Starting...")
global_start = time.perf_counter()
for s in slices:
    query_slice_queue.put(s)

query_slice_queue.join()
save_query_queue.join()

print(f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] Joining results")
results = []
individual_times_secs = 0
retrieved_rows = 0
while not results_queue.empty():
    r = results_queue.get()
    year = r["year"]
    week_number = r["week_number"]
    query_time_secs = r["slice_query_ns"] / 1_000_000_000.0
    save_time_secs = r["save_query_ns"] / 1_000_000_000.0
    rows = r["rows"]
    retrieved_rows += rows
    individual_times_secs += query_time_secs + save_time_secs
    print(
        f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] {y}-{w:0>2}: "
        f"rows: {rows: >10,}, "
        f"query: {query_time_secs: >18,.6f} secs, "
        f"save: {save_time_secs: >18,.6f} secs, "
        f"query speed: {rows/query_time_secs: >18,.6f} rows/sec, "
        f"save speed: {rows/save_time_secs: >18,.6f} rows/sec, "
        f"overall speed {rows/(query_time_secs+save_time_secs): >18,.6f} rows/sec"
    )
    results_queue.task_done()

global_elapsed_secs = time.perf_counter() - global_start

print(
    f"ROWS   : Expected {EXPECTED_TOTAL_ROWS: >18,} {'==' if EXPECTED_TOTAL_ROWS == retrieved_rows else '!='} {retrieved_rows: >18,} Retrieved"
)
print(
    f"SECONDS: Elapsed  {global_elapsed_secs: >18,.6f} {' <' if global_elapsed_secs < individual_times_secs else '>='} {individual_times_secs: >18,.6f} Total indiviual times"
)

print(f"ROWS/SEC: {retrieved_rows/global_elapsed_secs: >18,.6f}")

print(f"{'='*40}  DONE  {'='*40}")
