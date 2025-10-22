from typing import List
from src.models.spar_models import SparProductGroups
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class ProductGroupsRepository(BaseRepository[SparProductGroups]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparProductGroups]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparProductGroups(
                    code1=row.code1, name1=row.name1,
                    code2=row.code2, name2=row.name2,
                    code3=row.code3, name3=row.name3,
                    code4=row.code4, name4=row.name4,
                    code5=row.code5, name5=row.name5,
                    # code6=row.code6, name6=row.name6,
                    # code7=row.code7, name7=row.name7,
                    # code8=row.code8, name8=row.name8,
                    # code9=row.code9, name9=row.name9,
                    # code10=row.code10, name10=row.name10,
                    # code11=row.code11, name11=row.name11,
                    # code12=row.code12, name12=row.name12,
                    # code13=row.code13, name13=row.name13,
                    # code14=row.code14, name14=row.name14,
                    # code15=row.code15, name15=row.name15
                )
                for row in results
            ]
        finally:
            self.db.close()
