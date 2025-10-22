# RELEX Sync

Sincronizador de datos entre sistemas internos (SPAR) y el entorno RELEX.  
Genera ficheros CSV con datos normalizados y los publica en Azure Blob Storage (ABS).

---

## Estructura del proyecto

```

relex_sync/
│
├── output/                  # CSV generados listos para exportar
│
├── scripts/
│   └── upload.ps1   # Script PowerShell que sube los CSV a Azure Blob Storage
│
├── src/
│   ├── config/              # Configuración de interfaces y SQL de origen
│   ├── mappers/             # Transformadores SPAR → RELEX
│   ├── models/              # Modelos Pydantic para validación
│   ├── repositories/        # Repositorios (lectura de SQL Server)
│   ├── services/            # Lógica de orquestación, validación y exportación
│   └── utils/               # Utilidades (DB, CSV, export, formatos)
│
├── .env                     # Variables de entorno (credenciales, BD, ABS)
├── .env.example             # Ejemplo de configuración
├── README.md
└── venv/                    # Entorno virtual de Python

````

---

## Requisitos

- **Windows Server o Windows 10+ x64**
- **Python 3.12+** (validado también con 3.14)
- **Microsoft ODBC Driver 18 for SQL Server (x64)**
- **AzCopy v10.30+** instalado o descomprimido localmente

---

## Configuración inicial

### 1. Clonar o copiar el proyecto
```powershell
cd C:\apps
git clone <repo_url> relex_sync
cd relex_sync
````

### 2. Crear y activar el entorno virtual

```powershell
& "C:\Program Files\Python\python.exe" -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```powershell
pip install -U pip wheel setuptools
pip install pandas pydantic pyodbc python-dotenv
```

### 4. Instalar el driver SQL

[Descargar ODBC Driver 18 for SQL Server (x64)](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server)

### 5. Configurar el archivo `.env` (copiar desde `.env.example` y completar):

```bash
   DB_DRIVER=ODBC Driver 18 for SQL Server
   DB_SERVER=xxxxxx
   DB_DATABASE=xxxxxx
   DB_USERNAME=xxxxxx
   DB_PASSWORD=xxxxxx
   DB_ENCRYPT=xxxxxx
   DB_TRUST_CERT=xxxxxx

   AZCOPY_APPLICATION_ID=xxxxxx
   AZCOPY_TENANT_ID=xxxxxx
   AZCOPY_CLIENT_SECRET=xxxxxx
   AZCOPY_DEST_URL=xxxxxx
````

---

## Ejecución manual

### Generar ficheros CSV

```powershell
.\.venv\Scripts\Activate.ps1
python -m src.main 
python -m src.main products
```

Los ficheros se generan en `output/`.

### Subir a Azure Blob Storage

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\upload.ps1
```

---

## Pruebas de conexión

Verifica las conexiones a la base de datos y RELEX antes de la primera ejecución:

```powershell
python test_connection.py
python test_all_connections.py
```

---

## Salidas esperadas

Los ficheros CSV generados siguen la convención:

```
<interfaz>_YYYY-MM-DD_HHMMSS.csv
```

Ejemplo:

```
products_2025-10-21_113853.csv
locations_2025-10-21_095829.csv
```

**Versión inicial:** Octubre 2025

```
