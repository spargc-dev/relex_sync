from typing import List
from src.models.spar_models import SparSalesPrices
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection
from datetime import date, datetime

from datetime import date, datetime

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
                    start_date=self._parse_date(row.start_date),
                    end_date=self._parse_date(row.end_date),
                    sales_price=row.sales_price,
                    sales_price_with_vat=row.sales_price_with_vat,
                    price_type=row.price_type,
                    Igic=row.Igic,
                )
                for row in results
            ]
        finally:
            self.db.close()

    @staticmethod
    def _parse_date(value):
        """Convierte a date o None valores vacíos o incorrectos."""
        if value in (None, "", " ", "NULL"):
            return None
        if isinstance(value, date):
            return value
        try:
            return datetime.strptime(str(value).strip(), "%Y-%m-%d").date()
        except Exception:
            return None
