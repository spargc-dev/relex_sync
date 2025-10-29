from typing import List
from src.models.spar_models import SparLocations 
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection
from src.utils.export_config import ExportConfig

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
                    #buying_forbidden=row.buying_forbidden,
                    #latitude=row.latitude,
                    #longitude=row.longitude,
                    location_opening_date=row.location_opening_date,
                    location_closing_date=row.location_closing_date,
                    reference_code=(
                        int(row.reference_code)
                        if str(row.reference_code).strip() not in ("", "None", "NULL", None)
                        else None
                    ),
                    #store_net_sales_area=row.store_net_sales_area,
                    store_size=row.store_size,
                    #custom_store_size_category=row.custom_store_size_category,
                    # timezone=row.timezone,
                    postal_code=ExportConfig.clean_postal_code(row.postal_code),
                    #timezone=row.timezone,
                    #custom_distibutor_id=row.postacustom_distibutor_idl_code,
                    #custom_distibutor_name=row.custom_distibutor_name,
                    #custom_store_zone=row.custom_store_zone,
                    #custom_store_partner=row.custom_store_partner,
                    #block_start_date=row.block_start_date,
                    #block_end_date=row.block_end_date,
                    custom_tarifa=row.custom_tarifa
                )
                for row in results
            ]
        finally:
            self.db.close()
