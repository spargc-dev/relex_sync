from typing import List
from src.models.spar_models import SparSales
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection
from src.utils.export_config import ExportConfig

class SalesRepository(BaseRepository[SparSales]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparSales]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparSales(
                    receipt_timestamp=row.receipt_timestamp,
                    receipt_code=row.receipt_code,
                    date=row.date,
                    time=row.time,
                    location=row.location,
                    product=row.product,
                    Quantity=row.Quantity,
                    receipt_row_number=row.receipt_row_number,
                    sales_value_with_tax=row.sales_value_with_tax,
                    pos_transactions=row.pos_transactions
                )
                for row in results
            ]
        finally:
            self.db.close()
