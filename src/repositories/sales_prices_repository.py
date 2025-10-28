from typing import List
from src.models.spar_models import SparSalesPrices
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class SalesPricesRepository(BaseRepository[SparSalesPrices]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparSalesPrices]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparSalesPrices(
                    product=row.product,
                    location=row.location,
                    start_date=row.start_date, 
                    end_date=row.end_date,
                    sales_price=row.sales_price,
                    sales_price_with_vat=row.sales_price_with_vat,
                    price_type=row.price_type,
                    Igic=row.Igic
                )
                for row in results
            ]
        finally:
            self.db.close()
