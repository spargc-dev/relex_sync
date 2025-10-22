from src.models.spar_models import SparProductGroups
from src.models.relex_models import RelexProductGroups
from src.mappers.base_mapper import BaseMapper
from src.utils.export_config import ExportConfig

class ProductGroupsMapper(BaseMapper[SparProductGroups, RelexProductGroups]):
    def map(self, source: SparProductGroups) -> RelexProductGroups:
        return RelexProductGroups(
            code1=ExportConfig.clean_code(source.code1),
            name1=ExportConfig.clean_string(source.name1),
            code2=ExportConfig.clean_code(source.code2) if source.code2 else None,
            name2=ExportConfig.clean_string(source.name2) if source.name2 else None,
            code3=ExportConfig.clean_code(source.code3) if source.code3 else None,
            name3=ExportConfig.clean_string(source.name3) if source.name3 else None,
            code4=ExportConfig.clean_code(source.code4) if source.code4 else None,
            name4=ExportConfig.clean_string(source.name4) if source.name4 else None,
            code5=ExportConfig.clean_code(source.code5) if source.code5 else None,
            name5=ExportConfig.clean_string(source.name5) if source.name5 else None,
            # code6=ExportConfig.clean_code(source.code6) if source.code6 else None,
            # name6=ExportConfig.clean_string(source.name6) if source.name6 else None,
            # code7=ExportConfig.clean_code(source.code7) if source.code7 else None,
            # name7=ExportConfig.clean_string(source.name7) if source.name7 else None,
            # code8=ExportConfig.clean_code(source.code8) if source.code8 else None,
            # name8=ExportConfig.clean_string(source.name8) if source.name8 else None,
            # code9=ExportConfig.clean_code(source.code9) if source.code9 else None,
            # name9=ExportConfig.clean_string(source.name9) if source.name9 else None,
            # code10=ExportConfig.clean_code(source.code10) if source.code10 else None,
            # name10=ExportConfig.clean_string(source.name10) if source.name10 else None,
            # code11=ExportConfig.clean_code(source.code11) if source.code11 else None,
            # name11=ExportConfig.clean_string(source.name11) if source.name11 else None,
            # code12=ExportConfig.clean_code(source.code12) if source.code12 else None,
            # name12=ExportConfig.clean_string(source.name12) if source.name12 else None,
            # code13=ExportConfig.clean_code(source.code13) if source.code13 else None,
            # name13=ExportConfig.clean_string(source.name13) if source.name13 else None,
            # code14=ExportConfig.clean_code(source.code14) if source.code14 else None,
            # name14=ExportConfig.clean_string(source.name14) if source.name14 else None,
            # code15=ExportConfig.clean_code(source.code15) if source.code15 else None,
            # name15=ExportConfig.clean_string(source.name15) if source.name15 else None,
        )
    