from typing import List
from src.models.spar_models import SparPromotionsCompetitorPrices
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class PromotionsCompetitorPricesRepository(BaseRepository[SparPromotionsCompetitorPrices]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparPromotionsCompetitorPrices]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparPromotionsCompetitorPrices(
                    observed_at=row.observed_at,
                    product=row.product,
                    competitor=row.competitor,
                    location=row.location,
                    location_attribute_name=row.location_attribute_name,
                    type=row.type,
                    sales_price=row.sales_price
                )
                for row in results
            ]
        finally:
            self.db.close()
