from typing import Set
from datetime import date, datetime, timezone, timedelta
from typing import Optional

class ExportConfig:
    OUTPUT_DIR: str = "output"
    DELIMITER: str = ";"
    ENCODING: str = "utf-8"
    HEADER: bool = True
    LINE_TERMINATOR: str = "\n"
    DATE_FORMAT: str = "%Y-%m-%d"
    DECIMAL: str = "."
    ESCAPE_BACKSLASH: bool = True

    # Si quieres conservar la lista para Space & Floor, mantenla, pero evita '"', ';', ','
    FORBIDDEN_CHARS: Set[str] = {
        "#", "%", "*", "{", "}", ":", "<", ">", "?", "/", "+", "|"
        # ojo: no incluimos '"', ';' ni ',' aquí para no alterar el contenido
    }

    @classmethod
    def clean_string(cls, value: str) -> str:
        if not isinstance(value, str):
            return value
        s = value
        # saneo "suave" para nombres (opcional):
        for ch in cls.FORBIDDEN_CHARS:
            s = s.replace(ch, "_")
        # NO tocar comillas ni punto y coma: el CSV las gestiona
        if cls.ESCAPE_BACKSLASH:
            s = s.replace("\\", "\\\\")
        return s

    @classmethod
    def clean_code(cls, value: str) -> str | None:
        if value is None:
            return None
        s = str(value)
        s = s.replace("?", "0").replace("#", "0")
        if cls.ESCAPE_BACKSLASH:
            s = s.replace("\\", "\\\\")
        return s

    @classmethod
    def format_date(cls, date: datetime) -> str:
        if not isinstance(date, datetime):
            return date
        return date.strftime(cls.DATE_FORMAT)

    @classmethod
    def clean_postal_code(cls, value) -> str | None:
        if value in (None, "", "NULL"):
            return None
        try:
            return str(int(float(value)))
        except (ValueError, TypeError):
            return str(value).strip()

    @classmethod
    def _parse_date(cls, value):
        if value in (None, "", " ", "NULL"):
            return None
        if isinstance(value, date):
            return value
        try:
            return datetime.strptime(str(value).strip(), "%Y-%m-%d").date()
        except Exception:
            return None
    
    @classmethod
    def normalize_timestamp(cls, ts) -> Optional[str]:
        """Devuelve timestamp ISO-8601 (2025-10-29T15:18:16+02:00) o None."""
        if ts is None:
            return None

        tz = timezone(timedelta(hours=2))

        if isinstance(ts, datetime):
            return ts.replace(tzinfo=tz).isoformat(timespec="seconds")

        if isinstance(ts, str):
            s = ts.strip()
            # Si viene como '2025-10-29 15:18:16' ⇒ convertir a '2025-10-29T15:18:16+02:00'
            if "T" not in s and " " in s:
                s = s.replace(" ", "T")
            if "+" not in s and "Z" not in s:
                s += "+02:00"
            return s

        return str(ts)
    
    @classmethod
    def normalize_time(cls, value) -> Optional[str]:
        """
        Normaliza un valor de hora a formato HH:mm.
        Funciona para valores string ('19:52:00.0000000', '19:52:00') y datetime.time.
        Devuelve SIEMPRE un string 'HH:MM' o None.
        """
        if value in (None, "", "NULL", " "):
            return None

        # Si es datetime.time → convertir a HH:MM
        from datetime import time as dtime
        if isinstance(value, dtime):
            return f"{value.hour:02d}:{value.minute:02d}"

        # Si es texto → limpiar segundos y microsegundos
        if isinstance(value, str):
            s = value.strip()
            if '.' in s:  # quitar microsegundos
                s = s.split('.')[0]
            parts = s.split(':')
            if len(parts) >= 2:
                # Forzar siempre HH:MM (sin segundos)
                return f"{int(parts[0]):02d}:{int(parts[1]):02d}"
            return s[:5]

        # Fallback genérico
        try:
            return str(value)[:5]
        except Exception:
            return None
