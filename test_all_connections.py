import pyodbc
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def try_connection(description, conn_str):
    logging.info(f"\nProbando conexión: {description}")
    logging.info("-" * 50)
    logging.info(f"Cadena de conexión: {conn_str}")
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT @@version")
        version = cursor.fetchone()[0]
        logging.info("¡CONEXIÓN EXITOSA!")
        logging.info(f"Versión SQL Server: {version}")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return False

def main():
    # Lista de configuraciones a probar
    configs = [
        ("Driver 17 + Windows Auth + No Encrypt", 
         "Driver={ODBC Driver 17 for SQL Server};"
         "Server=192.168.19.214;"
         "Database=RELEX;"
         "Trusted_Connection=yes;"
         "Encrypt=no;"),
        
        ("Driver 17 + Windows Auth + Trust Certificate", 
         "Driver={ODBC Driver 17 for SQL Server};"
         "Server=192.168.19.214;"
         "Database=RELEX;"
         "Trusted_Connection=yes;"
         "TrustServerCertificate=yes;"),
        
        ("Driver 17 + SQL Auth + No Encrypt",
         "Driver={ODBC Driver 17 for SQL Server};"
         "Server=192.168.19.214;"
         "Database=RELEX;"
         "Uid=Relex;"
         "Pwd=R3l3x22349%$par;"
         "Encrypt=no;"),
        
        ("Driver 17 + SQL Auth + Trust Certificate",
         "Driver={ODBC Driver 17 for SQL Server};"
         "Server=192.168.19.214;"
         "Database=RELEX;"
         "Uid=Relex;"
         "Pwd=R3l3x22349%$par;"
         "TrustServerCertificate=yes;"),
        
        ("Driver 18 + SQL Auth + Trust Certificate",
         "Driver={ODBC Driver 18 for SQL Server};"
         "Server=192.168.19.214;"
         "Database=RELEX;"
         "Uid=Relex;"
         "Pwd=R3l3x22349%$par;"
         "TrustServerCertificate=yes;"),
        
        ("Driver 17 + SQL Auth + Puerto Explícito",
         "Driver={ODBC Driver 17 for SQL Server};"
         "Server=192.168.19.214,1433;"
         "Database=RELEX;"
         "Uid=Relex;"
         "Pwd=R3l3x22349%$par;"
         "TrustServerCertificate=yes;"),
    ]
    
    # Probar cada configuración
    successful = False
    for desc, conn_str in configs:
        if try_connection(desc, conn_str):
            successful = True
            logging.info("\n¡Configuración exitosa encontrada!")
            logging.info(f"Usar esta configuración: {desc}")
            break
        
    if not successful:
        logging.error("\nNinguna configuración funcionó. Verificar:")
        logging.error("1. El servidor está encendido y accesible")
        logging.error("2. El firewall permite conexiones")
        logging.error("3. SQL Server acepta conexiones remotas")
        logging.error("4. Las credenciales son correctas")

if __name__ == "__main__":
    main()