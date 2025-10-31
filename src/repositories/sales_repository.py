from typing import List
from src.models.spar_models import SparSales
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection
from datetime import date, time
from src.utils.export_config import ExportConfig

class SalesRepository(BaseRepository[SparSales]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparSales]:
        try:
            results = self.db.execute_query(self.sql)
            mapped_results = []
            for row in results:
                mapped_results.append(
                    SparSales(
                        receipt_timestamp=ExportConfig.normalize_timestamp(row.receipt_timestamp),
                        receipt_code=str(row.receipt_code) if row.receipt_code is not None else None,
                        date=row.date,
                        time=row.time,
                        location=str(row.location) if row.location is not None else None,
                        product=str(row.product) if row.product is not None else None,
                        quantity=row.quantity,
                        receipt_row_number=row.receipt_row_number,
                        value=row.value,
                        sales_value_with_tax=row.sales_value_with_tax,
                        tax_amount=row.tax_amount,
                        sales_tax_rate=row.sales_tax_rate,
                        #campaign_code=row.campaign_code,
                        #transaction_campaign_code=row.transaction_campaign_code,
                        custom_supplier_cost=row.custom_supplier_cost
                    )
                )
            return mapped_results
        finally:
            self.db.close()
