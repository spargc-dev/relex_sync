from pydantic import BaseModel
from datetime import date

class RelexProductGroups(BaseModel):
    code1: str
    name1: str
    code2: str | None = None
    name2: str | None = None
    code3: str | None = None
    name3: str | None = None
    code4: str | None = None
    name4: str | None = None
    code5: str | None = None
    name5: str | None = None
    # code6: str | None = None
    # name6: str | None = None
    # code7: str | None = None
    # name7: str | None = None
    # code8: str | None = None
    # name8: str | None = None
    # code9: str | None = None
    # name9: str | None = None
    # code10: str | None = None
    # name10: str | None = None
    # code11: str | None = None
    # name11: str | None = None
    # code12: str | None = None
    # name12: str | None = None
    # code13: str | None = None
    # name13: str | None = None
    # code14: str | None = None
    # name14: str | None = None
    # code15: str | None = None
    # name15: str | None = None

class RelexCampaigns(BaseModel):
    campaign: int
    name: str
    start_date: date
    end_date: date
    state: str | None = None

class RelexSuppliers(BaseModel):
    supplier: int
    name: str
    #safety_lead_time: int | None = None 
    supplier_type: str | None = None # esto es enum
    #purchase_block: bool | None = None 
    incoterms: str | None = None
    currency: str | None = None

class RelexProducts(BaseModel):
    product: str
    name: str
    group: str 
    weight: float
    weight_unit: str
    ean: str | None = None
    # alternative_code: str | None = None
    # order_quantity: float | None = None
    # introduction_date: date | None = None
    # termination_date: date | None = None
    required_remaining_shelf_life: int | None = None
    reference_spoiling_time: int | None = None
    inventory_unit: str | None = None
    height: float | None = None
    depth: float | None = None
    width: float | None = None
    dimension_unit: str | None = None
    volume_unit: str | None = None
    volume: float | None = None
    box_size: float | None = None
    pallet_size: float | None = None
    # image_url: str | None = None
    # variant_type: str | None = None
    brand_code: str | None = None
    brand: str | None = None
    is_private_label: bool | None = None
    brand_tier: str | None = None
    # price_family: str | None = None
    line_group: str | None = None
    is_kvi: bool | None = None
    kvi_group: str | None = None
    supplier: str | None = None
    # manufacturer: str | None = None
    # merchandising_style: str | None = None
    # case_height: float | None = None
    # case_depth: float | None = None
    # case_width: float | None = None
    # case_units_high: int | None = None
    # case_units_deep: int | None = None
    # case_units_wide: int | None = None
    # case_pack_units: int | None = None
    # nesting_height: float | None = None
    # nesting_depth: float | None = None
    # nesting_width: float | None = None
    # squeeze_height: float | None = None
    # squeeze_depth: float | None = None
    # squeeze_width: float | None = None
    # tray_height: float | None = None
    # tray_depth: float | None = None
    # tray_width: float | None = None
    # tray_units_high: int | None = None
    # tray_units_deep: int | None = None
    # tray_units_wide: int | None = None
    # tray_pack_units: int | None = None
    # shape: str | None = None
    # peg_x: str | None = None
    # peg_y: str | None = None
    # number_of_peg_holes: int | None = None
    # peg_depth: float | None = None
    # max_stack: int | None = None
    # max_top_cap: int | None = None
    # max_right_cap: int | None = None
    # max_deep_cap: int | None = None
    # min_deep: int | None = None
    # max_deep: int | None = None
    # front_overhang: float | None = None
    # finger_space_above: float | None = None
    # finger_space_to_the_side: float | None = None
    # orientation_type: str | None = None # es enum
    # can_break_tray_up: bool | None = None
    # can_break_tray_down: bool | None = None
    # can_break_tray_top: bool | None = None
    # can_brak_tray_back: bool | None = None
    # merchandising_net_content: float | None = None
    # merchandising_unit_of_measure: str | None = None
    # sell_pack_count: int | None = None
    # sell_pack_description: str | None = None
    # sell_pack_product: str | None = None
    # reference_code: str | None = None
    custom_category: str | None = None
    custom_buyer: str | None = None
    custom_central: bool | None = None
    custom_selfcon: bool | None = None

class RelexLocations(BaseModel):
    location: int
    name: str
    currency: str | None = None
    chain: str | None = None
    country: str | None = None
    country_name: str | None = None
    city: str | None = None
    state_name: str | None = None
    region: str | None = None
    location_type: str | None = None # esto es un enum
    #buying_forbidden: str | None = None
    #latitude: float | None = None
    #longitude: float | None = None
    location_opening_date: date | None = None
    location_closing_date: date | None = None
    reference_code: int | None = None
    #store_net_sales_area: float | None = None
    store_size: float | None = None
    #custom_store_size_category: str | None = None
    # timezone: str | None = None
    postal_code: int | None = None
    #timezone: str | None = None
    #custom_distibutor_id: str | None = None
    #custom_distibutor_name: str | None = None
    #custom_store_zone: str | None = None
    #custom_store_partner: str | None = None
    #block_start_date: str | None = None
    #block_end_date: str | None = None
    custom_tarifa: str | None = None

class RelexProductLocations(BaseModel):
    product: int
    location: int
    supplier: int
    purchase_price: float
    book_value: float | None = None 
    sales_price: float | None = None 
    #sales_tax_rate: float | None = None 
    order_quantity: int | None = None 
    minimum_delivery_batch: float | None = None 
    #max_lot_size: float | None = None 
    #ugly_shelf_point: int | None = None 
    #shelf_pace: int | None = None 
    #introduction_date: date | None = None 
    #termination_date: date | None = None 
    #season_start: date | None = None 
    #season_end: date | None = None 
    reference_spoiling_time: date | None = None 
    #required_remaining_shelf_life: date | None = None 
    #production_lead_time: date | None = None 
    box_size: int | None = None 
    pallet_size: int | None = None 
    #pallet_layer_size: int | None = None 
    #invetory_unit_in_consumer_units: date | None = None 
    assortment_status: str | None = None 
    #shelving_delay: date | None = None 
    #legal_for_merchandising: date | None = None 
    #ilegal_for_merchandising: date | None = None 
    #reference_code: date | None = None 
    #reference_location_code: date | None = None 
    custom_NT: str | None = None
    # custom_prevision_abierta: str | None = None

class RelexSalesPrices(BaseModel):
    product: int
    location: int
    start_date:date 
    end_date: date | None = None
    sales_price: str | None = None
    sales_price_with_vat: float | None = None
    price_type: str | None = None
    Igic: float | None = None
    