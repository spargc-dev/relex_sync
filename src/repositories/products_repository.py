from typing import List
from src.models.spar_models import SparProducts
from src.repositories.base_repository import BaseRepository
from src.utils.db_connection import DatabaseConnection

class ProductsRepository(BaseRepository[SparProducts]):
    def __init__(self, sql: str):
        self.db = DatabaseConnection()
        self.sql = sql

    def get_all(self) -> List[SparProducts]:
        try:
            results = self.db.execute_query(self.sql)
            return [
                SparProducts(
                    product=row.product,
                    name=row.name,
                    group=row.group,
                    weight=row.weight,
                    weight_unit=row.weight_unit,
                    ean=row.ean,
                    # alternative_code=row.alternative_code,
                    # order_quantity=row.order_quantity,
                    # introduction_date=row.introduction_date,
                    # termination_date=row.termination_date,
                    required_remaining_shelf_life=row.required_remaining_shelf_life,
                    reference_spoiling_time=row.reference_spoiling_time,
                    inventory_unit=row.inventory_unit,
                    height=row.height,
                    depth=row.depth,
                    width=row.width,
                    dimension_unit=row.dimension_unit,
                    volume_unit=row.volume_unit,
                    volume=row.volume,
                    box_size=row.box_size,
                    pallet_size=row.pallet_size,
                    # image_url=row.image_url,
                    # variant_type=row.variant_type,
                    brand_code=row.brand_code,
                    brand=row.brand,
                    is_private_label=row.is_private_label,
                    brand_tier=row.brand_tier,
                    # price_family=row.price_family,
                    line_group=row.line_group,
                    is_kvi=row.is_kvi,
                    kvi_group=row.kvi_group,
                    supplier=row.supplier,
                    # manufacturer=row.manufacturer,
                    # merchandising_style=row.merchandising_style,
                    # case_height=row.case_height,
                    # case_depth=row.case_depth,
                    # case_width=row.case_width,
                    # case_units_high=row.case_units_high,
                    # case_units_deep=row.case_units_deep,
                    # case_units_wide=row.case_units_wide,
                    # case_pack_units=row.case_pack_units,
                    # nesting_height=row.nesting_height,
                    # nesting_depth=row.nesting_depth,
                    # nesting_width=row.nesting_width,
                    # squeeze_height=row.squeeze_height,
                    # squeeze_depth=row.squeeze_depth,
                    # squeeze_width=row.squeeze_width,
                    # tray_height=row.tray_height,
                    # tray_depth=row.tray_depth,
                    # tray_width=row.tray_width,
                    # tray_units_high=row.tray_units_high,
                    # tray_units_deep=row.tray_units_deep,
                    # tray_units_wide=row.tray_units_wide,
                    # tray_pack_units=row.tray_pack_units,
                    # shape=row.shape,
                    # peg_x=row.peg_x,
                    # peg_y=row.peg_y,
                    # number_of_peg_holes=row.number_of_peg_holes,
                    # peg_depth=row.peg_depth,
                    # max_stack=row.max_stack,
                    # max_top_cap=row.max_top_cap,
                    # max_right_cap=row.max_right_cap,
                    # max_deep_cap=row.max_deep_cap,
                    # min_deep=row.min_deep,
                    # max_deep=row.max_deep,
                    # front_overhang=row.front_overhang,
                    # finger_space_above=row.finger_space_above,
                    # finger_space_to_the_side=row.finger_space_to_the_side,
                    # orientation_type=row.orientation_type,
                    # can_break_tray_up=row.can_break_tray_up,
                    # can_break_tray_down=row.can_break_tray_down,
                    # can_break_tray_top=row.can_break_tray_top,
                    # can_brak_tray_back=row.can_brak_tray_back,
                    # merchandising_net_content=row.merchandising_net_content,
                    # merchandising_unit_of_measure=row.merchandising_unit_of_measure,
                    # sell_pack_count=row.sell_pack_count,
                    # sell_pack_description=row.sell_pack_description,
                    # sell_pack_product=row.sell_pack_product,
                    # reference_code=row.reference_code
                    custom_category=row.custom_category,
                    custom_buyer=row.custom_buyer,
                    custom_central=row.custom_central,
                    custom_selfcon=row.custom_selfcon
                )
                for row in results
            ]
        finally:
            self.db.close()
