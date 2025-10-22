# src/repositories/campaigns_repository.py
from typing import List
from src.models.spar_models import SparCampaigns
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class CampaignsRepository(BaseRepository[SparCampaigns]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparCampaigns]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparCampaigns(
                    campaign=row.campaign,
                    name=row.name,
                    start_date=row.start_date,
                    end_date=row.end_date,
                )
                for row in results
            ]
        finally:
            self.db.close()
