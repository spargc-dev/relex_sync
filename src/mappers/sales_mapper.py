from src.models.spar_models import SparSales
from src.models.relex_models import RelexSales
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig
from datetime import timezone, timedelta, datetime

class SalesMapper(BaseMapper[SparSales, RelexSales]):
    def map(self, source: SparSales) -> RelexSales:
        tz = timezone(timedelta(hours=2))  # UTC+02:00 → España en horario de verano
        receipt_ts_iso = None

        ts = source.receipt_timestamp

        # ⚙️ Paso 1: proteger tipos raros (de PyODBC, pandas, etc.)
        # Si no es datetime puro de Python, convertir a texto y normalizar
        if isinstance(ts, datetime):
            receipt_ts_iso = ts.replace(tzinfo=tz).isoformat(timespec="seconds")
        else:
            # Entra aquí si es str u otro tipo (decimal, pyodbc.Timestamp, etc.)
            receipt_ts_iso = ExportConfig.normalize_timestamp(str(ts)) if ts else None

        return RelexSales(
            receipt_timestamp=receipt_ts_iso,  # "2020-02-20T20:02:20+02:00"
            receipt_code=source.receipt_code,
            date=source.date,
            time=source.time,
            location=source.location,
            product=source.product,
            quantity=source.quantity,
            receipt_row_number=source.receipt_row_number,
            value=source.value,
            sales_value_with_tax=source.sales_value_with_tax,
            tax_amount=source.tax_amount,
            sales_tax_rate=source.sales_tax_rate,
            purchase_price=source.purchase_price,
            #campaign_code=source.campaign_code,
            #transaction_campaign_code=source.transaction_campaign_code,
            custom_supplier_cost=source.custom_supplier_cost
        )
