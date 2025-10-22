import os, pyodbc
from typing import Any
from dotenv import load_dotenv

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        load_dotenv()
        driver   = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
        server   = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        uid      = os.getenv("DB_USER")
        pwd      = os.getenv("DB_PASSWORD")
        encrypt  = os.getenv("DB_ENCRYPT", "no")
        trust    = os.getenv("DB_TRUST", "yes")
        self.conn_str = (
            f"Driver={{{driver}}};"
            f"Server={server};"
            f"Database={database};"
            f"Uid={uid};Pwd={pwd};"
            f"Encrypt={encrypt};TrustServerCertificate={trust};"
        )
        self._connection = None

    def get_connection(self) -> pyodbc.Connection:
        """Obtiene una conexión a la base de datos."""
        if self._connection is None:
            try:
                self._connection = pyodbc.connect(self.conn_str)
            except pyodbc.Error as e:
                raise Exception(f"Error connecting to database: {str(e)}")
        return self._connection

    def execute_query(self, query: str, params: tuple = None) -> Any:
        """
        Ejecuta una consulta SQL y devuelve los resultados.
        
        Args:
            query: La consulta SQL a ejecutar
            params: Parámetros opcionales para la consulta
        """
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                
            results = cursor.fetchall()
            cursor.close()
            return results
            
        except pyodbc.Error as e:
            raise Exception(f"Error executing query: {str(e)}")

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self._connection:
            self._connection.close()
            self._connection = None