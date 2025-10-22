from datetime import datetime, date
import pandas as pd
import uuid

class FileNamer:
    @staticmethod
    def build_filename(interface_name: str,
                       df_out: pd.DataFrame,
                       filename_date_fields: list[str],
                       unique_id_mode: str) -> str:
        # fecha de contenido: max() de los campos listados
        cdate = None
        for c in filename_date_fields or []:
            if c in df_out.columns:
                s = pd.to_datetime(df_out[c], errors="coerce")
                m = s.max()
                if pd.notna(m):
                    cdate = m.date() if cdate is None or m.date() > cdate else cdate
        if cdate is None:
            cdate = date.today()
        cdate_txt = cdate.strftime("%Y-%m-%d")

        uid = uuid.uuid4().hex[:8] if unique_id_mode == "uuid" \
            else datetime.now().strftime("%H%M%S")
        return f"{interface_name}_{cdate_txt}_{uid}.csv"
