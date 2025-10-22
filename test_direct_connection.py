import pyodbc

def test_connection():
    # Probamos con autenticación integrada de Windows
    conn_str = (
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=192.168.19.214;'
        'Database=RELEX;'
        'Trusted_Connection=yes;'
        'Encrypt=no;'
    )
    
    try:
        print("Intentando conectar con la cadena de conexión exacta...")
        conn = pyodbc.connect(conn_str)
        print("¡Conexión exitosa!")
        
        cursor = conn.cursor()
        cursor.execute("SELECT @@version")
        row = cursor.fetchone()
        print("\nVersión del servidor SQL:")
        print(row[0])
        
        cursor.close()
        conn.close()
        
    except pyodbc.Error as e:
        print("Error de conexión:")
        print(str(e))

if __name__ == "__main__":
    test_connection()