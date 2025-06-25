import psycopg.conninfo
from psycopg_pool import ConnectionPool
import psycopg
import asyncio


class DB_Access:
    def __init__(
        self, db_host: str, db_port: int, db_name: str, db_user: str, db_pass: str
    ):
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.pool = None
        self.conninfo = psycopg.conninfo.make_conninfo(
            host=self.db_host, 
            port=self.db_port, 
            dbname=self.db_name, 
            user=self.db_user, 
            password=self.db_pass)
        print(f"{self.conninfo}")

    def SetupConnectionPool(self, min_size: int = 1, max_size: int = 3):

        self.pool = ConnectionPool(
            self.conninfo,
            min_size=min_size, 
            max_size=max_size)
        print(f"[SetupConnectionPool] connection string: {self.pool.conninfo}")

    
    @property
    def ConnectionPool(self):
        if self.pool is None:
            self.SetupConnectionPool()

        return self.pool
    
