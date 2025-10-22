# src/utils/csv_exporter.py
from typing import List, TypeVar, Type
from pydantic import BaseModel
import pandas as pd
from pathlib import Path
from src.utils.export_config import ExportConfig
import csv
import os

T = TypeVar('T', bound=BaseModel)

class CsvExporter:
    @staticmethod
    def export_to_csv(items: List[T], output_path: str) -> None:
        """
        Exporta una lista de modelos Pydantic a CSV cumpliendo la norma RELEX:
        - UTF-8
        - delimitador ';'
        - cabecera
        - comillas en todos los campos (QUOTE_ALL)
        - "" duplicadas automáticamente (doublequote=True)
        - backslash duplicado previamente (clean_string/clean_code)
        - escritura a .tmp y rename atómico
        """
        data = [item.model_dump() for item in items]  # Pydantic v2
        df = pd.DataFrame(data)

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = out.with_suffix(out.suffix + ".tmp")

        df.to_csv(
            tmp_path,
            index=False,
            sep=ExportConfig.DELIMITER,
            encoding=ExportConfig.ENCODING,
            header=ExportConfig.HEADER,
            lineterminator=ExportConfig.LINE_TERMINATOR,
            # CSV estricto RELEX:
            quoting=csv.QUOTE_ALL,
            quotechar='"',
            doublequote=True,
        )
        os.replace(tmp_path, out)
