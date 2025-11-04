from src.models.spar_models import SparPromotionsCompetitorPrices
from src.models.relex_models import RelexPromotionsCompetitorPrices
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class PromotionsCompetitorPricesMapper(BaseMapper[SparPromotionsCompetitorPrices, RelexPromotionsCompetitorPrices]):
    def map(self, source: SparPromotionsCompetitorPrices) -> RelexPromotionsCompetitorPrices:
        return RelexPromotionsCompetitorPrices(
            observed_at=source.observed_at,
            product=source.product,
            competitor=source.competitor,
            location=source.location,
            location_attribute_name=source.location_attribute_name,
            type=source.type,
            sales_price=source.sales_price
        )
