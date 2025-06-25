import inspect
from psycopg import extensions as ext
import psycopg
import sqlalchemy as sa

DB_STATUS = {
    ext.STATUS_READY: "ready",
    ext.STATUS_ASYNC: "async",
    ext.STATUS_BEGIN: "begin",
    ext.STATUS_IN_TRANSACTION: "in transaction",
    ext.STATUS_PREPARED: "prepared",
    ext.STATUS_SETUP: "setup",
    ext.STATUS_SYNC: "sync",
}
# Environment
DB_HOST = "oppy-db-01.cec.delllabs.net"  # 'oppy-db-01.cec.delllabs.net' # 'localhost'
DB_PORT = 5432
DB_NAME = "business_reporter"
DB_USER = "oppy"
DB_PASS = "Mars2004-2018"
# Connect to your postgres DB using psycopg2 directly
# conn = psycopg2.connect(dbname="airflow", user="airflow", password="Mars2004-2018", host="10.227.242.242", port="5432")
conn = psycopg.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)
print(
    f"connection status: {DB_STATUS[conn.status] if conn.status in DB_STATUS else f'UNKNOWN -> {conn.status}'}."
)

cursor = conn.cursor()
cursor.execute("SELECT datname FROM pg_database;")
rows = cursor.fetchall()
print(f"Databases:")
for row in rows:
    print(f"-\t{row[0]}")
cursor.close()

cursor = conn.cursor()
cursor.execute(
    "select table_name from information_schema.tables where table_schema not in ('pg_catalog', 'information_schema') "
)
rows = cursor.fetchall()
print(f"Tables:")
for row in sorted(rows):
    print(f"-\t{row[0]}")
cursor.close()

sqls = [
    "SELECT 'jira_issues' AS TableName, count(*) AS Rows FROM public.jira_issues;",
    "SELECT 'jira_assigned_transitions' AS TableName, count(*) AS Rows FROM public.jira_assigned_transitions;",
    "SELECT 'jira_comments' AS TableName, count(*) AS Rows FROM public.jira_comments;",
    "SELECT 'jira_descriptions' AS TableName, count(*) AS Rows FROM public.jira_descriptions;",
    "SELECT 'jira_state_transitions' AS TableName, count(*) AS Rows FROM public.jira_state_transitions;",
    "SELECT 'snow_incidents' AS TableName, count(*) AS Rows FROM public.snow_incidents;",
    "SELECT 'snow_assigned_transitions' AS TableName, count(*) AS Rows FROM public.snow_assigned_transitions;",
    "SELECT 'snow_changes' AS TableName, count(*) AS Rows FROM public.snow_changes;",
    "SELECT 'snow_comments' AS TableName, count(*) AS Rows FROM public.snow_comments;",
    "SELECT 'snow_descriptions' AS TableName, count(*) AS Rows FROM public.snow_descriptions;",
    "SELECT 'snow_state_transitions' AS TableName, count(*) AS Rows FROM public.snow_state_transitions;",
]
print(f"Rows in tables:")
for sql in sqls:
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f"-\t{row[0]}: {row[1]}")
    cursor.close()

cursor.close()

conn.close()

# Connect to your postgres DB using SQLalchemy
# engine = sa.create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)
# engine_conn = engine.connect()

# print(f"engine_conn.info: {engine_conn.info}")
# props = inspect.getmembers(engine_conn.info, lambda a: not(inspect.isroutine(a)))
# for prop in props:
#    print(f"prop: {prop}")

# Close the connection
# engine_conn.close()
