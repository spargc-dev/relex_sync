from src.models.spar_models import SparLocations
from src.models.relex_models import RelexLocations
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class LocationsMapper(BaseMapper[SparLocations, RelexLocations]):
    def map(self, source: SparLocations) -> RelexLocations:
        return RelexLocations(
            location=source.location,
            name=ExportConfig.clean_string(source.name),
            currency=ExportConfig.clean_string(source.currency),
            chain=ExportConfig.clean_string(source.chain),
            country=ExportConfig.clean_string(source.country),
            country_name=ExportConfig.clean_string(source.country_name),
            city=ExportConfig.clean_string(source.city),
            state_name=ExportConfig.clean_string(source.state_name),
            region=ExportConfig.clean_string(source.region),
            location_type=ExportConfig.clean_string(source.location_type), # esto es un enum
            #buying_forbidden=source.buying_forbidden
            #latitude=source.latitude,
            #longitude=source.longitude,
            location_opening_date=source.location_opening_date,
            location_closing_date=source.location_closing_date,
            reference_code=source.reference_code,
            #store_net_sales_area=source.store_net_sales_area,
            store_size=source.store_size,
            #custom_store_size_category=source.location_closincustom_store_size_categoryg_date,
            #timezone=ExportConfig.clean_string(source.timezone), 
            postal_code=ExportConfig.clean_postal_code(source.postal_code),
            #timezone=source.timezone,
            #custom_distibutor_id=source.custom_distibutor_id,
            #custom_distibutor_name=source.custom_distibutor_name,
            #custom_store_zone=source.custom_store_zone,
            #custom_store_partner=source.custom_store_partner,
            #block_start_date=source.block_start_date,
            #block_end_date=source.block_end_date,
            custom_tarifa=source.custom_tarifa
        )
