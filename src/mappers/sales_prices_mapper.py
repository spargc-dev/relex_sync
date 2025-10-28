from src.models.spar_models import SparSalesPrices
from src.models.relex_models import RelexSalesPrices
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class SalesPricesMapper(BaseMapper[SparSalesPrices, RelexSalesPrices]):
    def map(self, source: SparSalesPrices) -> RelexSalesPrices:
        return RelexSalesPrices(
            product=source.product,
            location=source.location,
            start_date=source.start_date,
            end_date=source.end_date,
            sales_price=source.sales_price,
            sales_price_with_vat=source.sales_price_with_vat,
            price_type=source.price_type,
            Igic=source.Igic
        )
