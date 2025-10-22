from src.models.spar_models import SparLocations
from src.models.relex_models import RelexLocations
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class LocationsMapper(BaseMapper[SparLocations, RelexLocations]):
    def map(self, source: SparLocations) -> RelexLocations:
        return RelexLocations(
            location=ExportConfig.clean_string(source.location),
            name=ExportConfig.clean_string(source.name),
            currency=ExportConfig.clean_string(source.currency),
            chain=ExportConfig.clean_string(source.chain),
            country=ExportConfig.clean_string(source.country),
            country_name=ExportConfig.clean_string(source.country_name),
            city=ExportConfig.clean_string(source.city),
            state_name=ExportConfig.clean_string(source.state_name),
            region=ExportConfig.clean_string(source.region),
            location_type=ExportConfig.clean_string(source.location_type), # esto es un enum
            latitude=source.latitude,
            longitude=source.longitude,
            location_opening_date=source.location_opening_date,
            location_closing_date=source.location_closing_date,
            store_net_sales_area=source.store_net_sales_area,
            store_size=source.store_size,
            timezone=ExportConfig.clean_string(source.timezone), 
            postal_code=ExportConfig.clean_string(source.postal_code)
        )
