from src.models.spar_models import SparSuppliers
from src.models.relex_models import RelexSuppliers
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class SuppliersMapper(BaseMapper[SparSuppliers, RelexSuppliers]):
    def map(self, source: SparSuppliers) -> RelexSuppliers:
        return RelexSuppliers(
            supplier=ExportConfig.clean_string(source.supplier),
            name=ExportConfig.clean_string(source.name),
            safety_lead_time=source.safety_lead_time,
            supplier_type=source.supplier_type,
            purchase_block=source.purchase_block,
            incoterms=ExportConfig.clean_string(source.incoterms),
            currency=ExportConfig.clean_string(source.currency)
        )
    