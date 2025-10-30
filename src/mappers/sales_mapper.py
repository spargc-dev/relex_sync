from src.models.spar_models import SparSales
from src.models.relex_models import RelexSales
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class SalesMapper(BaseMapper[SparSales, RelexSales]):
    def map(self, source: SparSales) -> RelexSales:
        return RelexSales(
            receipt_timestamp=source.receipt_timestamp,
            receipt_code=source.receipt_code,
            date=source.date,
            time=source.time,
            location=source.location,
            product=source.product,
            Quantity=source.Quantity,
            receipt_row_number=source.receipt_row_number,
            sales_value_with_tax=source.sales_value_with_tax,
            pos_transactions=source.pos_transactions
        )
