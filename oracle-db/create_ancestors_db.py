from sys import exit

import oracledb
from oracledb import DatabaseError, DataError, Error, IntegrityError, InterfaceError, InternalError, NotSupportedError, OperationalError, ProgrammingError, Warning

SQL_STMT_DEFINE_ANCESTORS=[
"""
CREATE TABLESPACE tbs_ancestors 
  DATAFILE 'ancestors.dbf' 
  SIZE 40M 
  ONLINE; 
""",
"""
CREATE USER scott 
   IDENTIFIED BY tiger
  DEFAULT TABLESPACE tbs_ancestors;
""",
"GRANT CONNECT TO scott;",
"GRANT RESOURCE TO scott;"
]

SQL_STMT_QUERY_TABLESPACES="""
SELECT TABLESPACE_NAME
FROM DBA_TABLESPACES
"""

SQL_STMT_DEFINE_PERSON="""
CREATE TABLE scott.Person (
 ID VARCHAR2(8) NOT NULL,
 FIRSTNAME VARCHAR2(30) NOT NULL,
 MIDDLE_NAMES VARCHAR2(200) NULL,
 LASTNAME_1 VARCHAR2(30) NOT NULL,
 LASTNAME_2 VARCHAR2(30) NOT NULL,
 BIRTHDAY DATE NOT NULL,
 DECEASED DATE NULL,
 BIRTH_COUNTRY VARCHAR2(30) NOT NULL,
 BIRTH_CITY VARCHAR2(30) NOT NULL,
 SEX CHAR(1) CHECK (SEX IN ('M', 'F')),
 FATHER VARCHAR2(8) NULL,
 MOTHER VARCHAR2(8) NULL,
 CONSTRAINT PERSON_TABLE_PK PRIMARY KEY (ID),
 CONSTRAINT PERSON_FATHER FOREIGN KEY (FATHER) REFERENCES scott.Person (ID),
 CONSTRAINT PERSON_MOTHER FOREIGN KEY (MOTHER) REFERENCES scott.Person (ID)
);
"""

SQL_STMT_QUERY_PERSON = """
SELECT *
FROM SCOTT.PERSON
"""

"""
admin_conn = oracledb.connect(user="SYSTEM", password="ABCdef123!", dsn="localhost:1521/FREEPDB1")

with admin_conn.cursor() as admin_cur:
   admin_cur.execute(SQL_STMT_QUERY_TABLESPACES)
   res = admin_cur.fetchall()
   if "tbs_ancestors".upper() in res:
      print("Defining ancestors...")
      for sql_stmt in SQL_STMT_DEFINE_ANCESTORS:
         try:
            admin_cur.execute(sql_stmt)
         except (DatabaseError,
                 DataError,
                 Error,
                 IntegrityError,
                 InterfaceError,
                 InternalError,
                 NotSupportedError,
                 OperationalError,
                 ProgrammingError,
                 Warning) as ex:
            print(f"{type(ex)=} at '{sql_stmt}'.")
            ora_err_obj, = ex.args
            print("Error Code:", ora_err_obj.code)
            print("Error Full Code:", ora_err_obj.full_code)
            print("Error Message:", ora_err_obj.message)
            exit()

      admin_cur.execute(SQL_STMT_TABLESPACES_DATAFILES)
      res = admin_cur.fetchall()
      if len(res) == 0:
         raise Exception('[DB ERROR] Failed to create Ancestors tablespace')
   else:
      print("ancestors already defined!")
      print(res)
"""

scott_conn = oracledb.connect(user="scott", password="tiger", dsn="localhost:1521/FREEPDB1")
with scott_conn.cursor() as scott_cur:
   #scott_cur.execute(SQL_STMT_DEFINE_TABLES)
   scott_cur.execute(SQL_STMT_QUERY_PERSON)
   res = scott_cur.fetchall()
   print(f"Totals rows in Person: {len(res)}")
