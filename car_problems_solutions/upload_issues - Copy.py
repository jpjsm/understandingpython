import psycopg
import csv
import hashlib

# Environment
DB_HOST = "localhost"  # 'oppy-db-01.cec.delllabs.net' # 'localhost'
DB_PORT = 5432
DB_NAME = "car_problems_solutions"
DB_USER = "postgres"
DB_PASS = "ABCdef123!"
# Connect to your postgres DB using psycopg2 directly
# conn = psycopg2.connect(dbname="airflow", user="airflow", password="Mars2004-2018", host="10.227.242.242", port="5432")
conn = psycopg.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)
print(f"connection status: {conn.info.status}.")

with conn.cursor() as cursor:
    cursor.execute("SELECT datname FROM pg_database;")
    rows = cursor.fetchall()
    print(f"Databases:")
    for row in rows:
        print(f"-\t{row[0]}")

with conn.cursor() as cursor:
    cursor.execute(
        "select table_schema, table_name from information_schema.tables where table_schema not in ('pg_catalog', 'information_schema') "
    )
    rows = cursor.fetchall()
    print(f"Tables:")
    for _schema, _tablename in sorted(rows):
        print(f"-\t{_schema}.{_tablename}")

with open("./car_problems_solution.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f"{row}")
        problem = row["PROBLEM"].lower().strip()
        solution = row["SOLUTION"].lower().strip()
        id = hashlib.sha256(str.encode(f"{problem}{solution}")).hexdigest()
        try:
            result = conn.execute(
                "INSERT INTO issues (id, problem, solution) VALUES(%s, %s, %s)",
                (id, problem, solution),
            )
            conn.commit()
        except psycopg.Error as ex:
            print(
                f"{ex.sqlstate=} | {ex.diag.severity=} | {ex.diag.message_primary=} | {ex.diag.message_detail=} | {ex.pgconn=} | {ex.pgresult=}"
            )
conn.close()
