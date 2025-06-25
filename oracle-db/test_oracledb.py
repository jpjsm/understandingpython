import oracledb

conn = oracledb.connect(user="pdbadmin", password="ABCdef123!", dsn="localhost:1521/FREEPDB1")
with conn.cursor() as cur:
   cur.execute("SELECT 'Hello World!' FROM dual")
   res = cur.fetchall()
   print(res)