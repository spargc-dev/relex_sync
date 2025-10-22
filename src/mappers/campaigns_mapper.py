# src/mappers/campaigns_mapper.py
from src.models.spar_models import SparCampaigns
from src.models.relex_models import RelexCampaigns
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class CampaignsMapper(BaseMapper[SparCampaigns, RelexCampaigns]):
    def map(self, source: SparCampaigns) -> RelexCampaigns:
        return RelexCampaigns(
            campaign=ExportConfig.clean_string(source.campaign),
            name=ExportConfig.clean_string(source.name),
            start_date=source.start_date,
            end_date=source.end_date,
        )
