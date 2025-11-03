from typing import List
from src.models.spar_models import SparProductLocations
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class ProductLocationsRepository(BaseRepository[SparProductLocations]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def _parse_bool(self, value):
        """Convierte valores SQL (0/1, '', None, etc.) a bool o None"""
        if value in (None, '', ' ', 'NULL'):
            return None  # o False si prefieres forzar
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return bool(value)
        s = str(value).strip().lower()
        if s in ('1', 'true', 't', 'yes', 'y', 'si'):
            return True
        if s in ('0', 'false', 'f', 'no', 'n'):
            return False
        return None

    def get_all(self) -> List[SparProductLocations]:
        try:
            results = self.db.execute_query(self.sql)
            mapped_results = []

            for row in results:
                mapped_results.append(
                    SparProductLocations(
                        product=row.product,
                        location=row.location,
                        supplier=row.supplier,
                        purchase_price=row.purchase_price,
                        book_value=row.book_value,
                        sales_price=row.sales_price,
                        sales_tax_rate=row.sales_tax_rate,
                        order_quantity=row.order_quantity,
                        minimum_delivery_batch=row.minimum_delivery_batch,
                        max_lot_size=row.max_lot_size,
                        #ugly_shelf_point=row.ugly_shelf_point,
                        #shelf_pace=row.shelf_pace,
                        #introduction_date=row.introduction_date,
                        #termination_date=row.termination_date,
                        #season_start=row.season_start,
                        #season_end=row.season_end,
                        reference_spoiling_time=row.reference_spoiling_time,
                        required_remaining_shelf_life=row.required_remaining_shelf_life,
                        production_lead_time=row.production_lead_time,
                        box_size=row.box_size,
                        pallet_size=row.pallet_size,
                        #pallet_layer_size=row.pallet_layer_size,
                        #invetory_unit_in_consumer_units=row.invetory_unit_in_consumer_units,
                        assortment_status=row.assortment_status,
                        #shelving_delay=row.shelving_delay,
                        #legal_for_merchandising=row.legal_for_merchandising,
                        #ilegal_for_merchandising=row.ilegal_for_merchandising,
                        #reference_code=row.reference_code,
                        #reference_location_code=row.reference_location_code,
                        custom_nt=self._parse_bool(row.custom_nt),
                        custom_prevision_abierta=self._parse_bool(row.custom_prevision_abierta)
                    )
                )

            return mapped_results
        finally:
            self.db.close()
