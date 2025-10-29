from typing import Set
from datetime import date, datetime

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
