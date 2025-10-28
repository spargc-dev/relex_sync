from typing import List
from src.models.spar_models import SparSuppliers
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class SuppliersRepository(BaseRepository[SparSuppliers]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparSuppliers]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparSuppliers(
                    supplier=row.supplier,
                    name=row.name,
                    #safety_lead_time=row.safety_lead_time,
                    supplier_type=row.supplier_type,
                    #purchase_block=row.purchase_block,
                    incoterms=row.incoterms,
                    currency=row.currency
                )
                for row in results
            ]
        finally:
            self.db.close()
