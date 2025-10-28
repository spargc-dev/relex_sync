from src.models.spar_models import SparProductLocations
from src.models.relex_models import RelexProductLocations
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class ProductLocationsMapper(BaseMapper[SparProductLocations, RelexProductLocations]):
    def map(self, source: SparProductLocations) -> RelexProductLocations:
        return RelexProductLocations(
            product=source.product,
            location=source.location,
            supplier=ExportConfig.clean_code(source.supplier),
            purchase_price=source.purchase_price,
            book_value=source.book_value,
            sales_price=source.sales_price,
            #sales_tax_rate=source.sales_tax_rate,
            order_quantity=source.order_quantity,
            minimum_delivery_batch=source.minimum_delivery_batch,
            #max_lot_size=source.max_lot_size,
            #ugly_shelf_point=source.ugly_shelf_point,
            #shelf_pace=source.shelf_pace,
            #introduction_date=source.introduction_date,
            #termination_date=source.termination_date,
            #season_start=source.season_start,
            #season_end=source.season_end,
            reference_spoiling_time=source.reference_spoiling_time,
            #required_remaining_shelf_life=source.required_remaining_shelf_life,
            #production_lead_time=source.production_lead_time,
            box_size=source.box_size,
            pallet_size=source.pallet_size,
            #pallet_layer_size=source.pallet_layer_size,
            #invetory_unit_in_consumer_units=source.invetory_unit_in_consumer_units,
            assortment_status=source.assortment_status,
            #shelving_delay=source.shelving_delay,
            #legal_for_merchandising=source.legal_for_merchandising, 
            #ilegal_for_merchandising=source.ilegal_for_merchandising,
            #reference_code=source.reference_code,
            #reference_location_code=source.reference_location_code,
            custom_NT=source.custom_NT,
            #custom_prevision_abierta=source.custom_prevision_abierta

        )