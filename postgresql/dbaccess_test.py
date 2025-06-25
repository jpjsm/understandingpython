from dbaccess import DB_Access

db = DB_Access(
    db_host='localhost', 
    db_port='5432', 
    db_name='icecream', 
    db_user='Yogi', 
    db_pass='ABCdef123!')
pool = db.ConnectionPool
print("pool created")
with pool.connection() as cnx:
    cursor = cnx.execute('SELECT * FROM public."Icecream"')
    rows = cursor.fetchall()
    print(rows)
