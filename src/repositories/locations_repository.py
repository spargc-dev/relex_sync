from typing import List
from src.models.spar_models import SparLocations 
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class LocationsRepository(BaseRepository[SparLocations]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparLocations]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparLocations(
                    location=row.location,
                    name=row.name,
                    currency=row.currency,
                    chain=row.chain,
                    country=row.country,
                    country_name=row.country_name,
                    city=row.city,
                    state_name=row.state_name,
                    region=row.region,
                    location_type=row.location_type,
                    latitude=row.latitude,
                    longitude=row.longitude,
                    location_opening_date=row.location_opening_date,
                    location_closing_date=row.location_closing_date,
                    store_net_sales_area=row.store_net_sales_area,
                    store_size=row.store_size,
                    timezone=row.timezone,
                    postal_code=row.postal_code,
                )
                for row in results
            ]
        finally:
            self.db.close()
