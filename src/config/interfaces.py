from dataclasses import dataclass, field
from typing import List, Dict, Tuple

@dataclass
class InterfaceConfig:
    interface_name: str
    source_sql: str
    filename_date_fields: List[str] = field(default_factory=list)
    unique_id_mode: str = "timestamp"
    required_non_null: List[str] = field(default_factory=list)
    unique_combo: List[List[str]] = field(default_factory=list)
    domain_checks: Dict[str, List] = field(default_factory=dict)
    date_order: List[Tuple[str, str]] = field(default_factory=list)

#===================
#   Product groups
#===================
PRODUCT_GROUPS = InterfaceConfig(
    interface_name="product_groups",
    source_sql="""
        SELECT
            code1 AS code1, name1 AS name1,
            code2 AS code2, name2 AS name2,
            code3 AS code3, name3 AS name3,
            code4 AS code4, name4 AS name4,
            code5 AS code5, name5 AS name5
            -- , code6 AS code6, name6 AS name6
            -- , code7 AS code7, name7 AS name7
            -- , code8 AS code8, name8 AS name8
            -- , code9 AS code9, name9 AS name9
            -- , code10 AS code10, name10 AS name10
            -- , code11 AS code11, name11 AS name11
            -- , code12 AS code12, name12 AS name12
            -- , code13 AS code13, name13 AS name13
            -- , code14 AS code14, name14 AS name14
            -- , code15 AS code15, name15 AS name15
        FROM [pub_md].[product_groups];
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=["code1", "name1"],
    # unique_combo=[["code1"],["code2"],["code3"],["code4"],["code5"],["code6"]],
    domain_checks={},
    date_order=[],
)

#=================================
#     Campaigns (History & daily)    
#=================================
CAMPAIGNS = InterfaceConfig(
    interface_name="campaigns",
    source_sql="""
        SELECT
            Codigo AS campaign,
            Nombre AS name,
            Fecha_Entrada AS start_date,
            Fecha_Salida AS end_date
        FROM [dbo].[INT_Product-location-campaigns]
        WHERE Fecha_Entrada >= '2023-01-01' OR Fecha_Salida >= '2023-01-01';
    """,
    filename_date_fields=["start_date", "end_date"],
    unique_id_mode="timestamp",
    required_non_null=["campaign", "name", "start_date", "end_date"],
    #domain_checks={
    #    "state": ["", "DELETE"]
    #},
    date_order=[("start_date", "end_date")],
)

#===========
# Suppliers 
#===========
SUPPLIERS = InterfaceConfig(
    interface_name="suppliers",
    source_sql="""
        SELECT
            supplier AS supplier, 
            name AS name, 
            -- , safety_lead_time AS safety_lead_time
            supplier_type AS supplier_type,
            -- , purchase_block AS purchase_block
            incoterms AS incoterms,
            currency AS currency
        FROM [pub_md].[suppliers];
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=["supplier", "name"],
    domain_checks={},
    date_order=[],
)

#===========
# Products 
#===========
PRODUCTS = InterfaceConfig(
    interface_name="products",
    source_sql="""
        SELECT
            product AS product, 
            name AS name, 
            [group] AS [group], 
            weight AS weight,
            weight_unit AS weight_unit,
            ean AS ean,
            -- , alternative_code AS alternative_code
            -- , order_quantity as order_quantity
            -- , introduction_date AS introduction_date
            -- , termination_date AS termination_date
            required_remaining_shelf_life AS required_remaining_shelf_life,
            reference_spoiling_time as reference_spoiling_time,
            inventory_unit AS inventory_unit,
            height AS height,
            depth AS depth,
            width AS width,
            dimension_unit AS dimension_unit,
            volume_unit AS volume_unit,
            volume AS volume,
            box_size AS box_size,
            pallet_size AS pallet_size,
            -- , image_url AS image_url
            -- , variant_type AS variant_type
            brand_code AS brand_code,
            brand AS brand,
            is_private_label AS is_private_label,
            brand_tier AS brand_tier,
            -- , price_family AS price_family
            line_group AS line_group,
            is_kvi AS is_kvi,
            kvi_group AS kvi_group,
            supplier as supplier,
            -- , manufacturer AS manufacturer
            -- , merchandising_style AS merchandising_style
            -- , case_height AS case_height
            -- , case_depth AS case_depth
            -- , case_width AS case_width
            -- , case_units_high AS case_units_high
            -- , case_units_deep AS case_units_deep
            -- , case_units_wide AS case_units_wide
            -- , case_pack_units AS case_pack_units
            -- , nesting_height AS nesting_height
            -- , nesting_depth AS nesting_depth
            -- , nesting_width AS nesting_width
            -- , squeeze_height AS squeeze_height
            -- , squeeze_depth AS squeeze_depth
            -- , squeeze_width AS squeeze_width
            -- , tray_height AS tray_height
            -- , tray_depth AS tray_depth
            -- , tray_width AS tray_width
            -- , tray_units_high AS tray_units_high
            -- , tray_units_deep AS tray_units_deep
            -- , tray_units_wide AS tray_units_wide
            -- , tray_pack_units AS tray_pack_units
            -- , shape AS shape
            -- , peg_x AS peg_x
            -- , peg_y AS peg_y
            -- , number_of_peg_holes AS number_of_peg_holes
            -- , peg_depth AS peg_depth
            -- , max_stack AS max_stack
            -- , max_top_cap AS max_top_cap
            -- , max_right_cap AS max_right_cap
            -- , max_deep_cap AS max_deep_cap
            -- , min_deep AS min_deep
            -- , max_deep AS max_deep
            -- , front_overhang AS front_overhang
            -- , finger_space_above AS finger_space_above
            -- , finger_space_to_the_side AS finger_space_to_the_side
            -- , orientation_type AS orientation_type
            -- , can_break_tray_up AS can_break_tray_up
            -- , can_break_tray_down AS can_break_tray_down
            -- , can_break_tray_top AS can_break_tray_top
            -- , can_break_tray_back AS can_brak_tray_back
            -- , merchandising_net_content AS merchandising_net_content
            -- , merchandising_unit_of_measure AS merchandising_unit_of_measure
            -- , sell_pack_count as sell_pack_count
            -- , sell_pack_description AS sell_pack_description
            -- , sell_pack_product as sell_pack_product
            -- , reference_code AS reference_code
            custom_category as custom_category,
            custom_buyer as custom_buyer,
            custom_central as custom_central,
            custom_selfcon as custom_selfcon
        FROM [pub_md].[products];
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=["product", "name", "group", "weight", "weight_unit"],
    domain_checks={},
    date_order=[],
)

#=================================
#     Locations  
#=================================
LOCATIONS = InterfaceConfig(
    interface_name="locations",
    source_sql="""
        SELECT
            location AS location,
            name AS name,
            currency AS currency,
            chain AS chain,
            country AS country,
            country_name AS country_name,
            city AS city,
            state_name AS state_name, 
            region AS region,
            location_type AS location_type,
            -- , buying_forbidden AS buying_forbidden
            -- , latitude AS latitude
            -- , longitude AS longitude
            -- , TRY_CONVERT(float, NULLIF(REPLACE(LTRIM(RTRIM(latitude)), ',', '.'), ''))  AS latitude
            -- , TRY_CONVERT(float, NULLIF(REPLACE(LTRIM(RTRIM(longitude)), ',', '.'), '')) AS longitude
            location_opening_date AS location_opening_date,
            location_closing_date AS location_closing_date,
            reference_code AS reference_code,
            -- , number_of_checkouts AS number_of_checkouts
            -- , store_net_sales_area AS store_net_sales_area
            store_size AS store_size,
            -- , custom_store_size_category AS custom_store_size_category
            -- , timezone AS timezone
            postal_code AS postal_code,
            -- , custom_distibutor_id AS custom_distibutor_id
            -- , custom_distibutor_name AS custom_distibutor_name
            -- , custom_store_zone AS custom_store_zone
            -- , custom_store_partner AS custom_store_partner 
            -- , block_start_date AS block_start_date
            -- , block_end_date AS block_end_date,
            custom_tarifa AS custom_tarifa
        FROM [pub_md].[locations]
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=["location", "name"],
    #domain_checks={
    #    "state": ["", "DELETE"]
    #},
    date_order=[],
)

#===================
#   Product locations
#===================
PRODUCT_LOCATIONS = InterfaceConfig(
    interface_name="product_locations",
    source_sql="""
        SELECT
            product AS product,
            location AS location,
            -- , CASE WHEN supplier = 9051 THEN 9050 ELSE supplier END AS supplier
            supplier AS supplier,
            purchase_price AS purchase_price,
            book_value AS book_value,
            sales_price AS sales_price,
            sales_tax_rate AS sales_tax_rate,
            order_quantity AS order_quantity,
            minimum_delivery_batch AS minimum_delivery_batch,
            max_lot_size AS max_lot_size,
            -- , ugly_shelf_point AS ugly_shelf_point
            -- , introduction_date AS introduction_date
            -- , termination_date AS termination_date
            -- , season_start AS season_start
            -- , season_end AS season_end
            reference_spoiling_time AS reference_spoiling_time,
            required_remaining_shelf_life AS required_remaining_shelf_life,
            production_lead_time AS production_lead_time,
            box_size AS box_size,
            pallet_size AS pallet_size,
            -- , pallet_layer_size AS pallet_layer_size
            -- , inventory_unit_in_consumer_units AS inventory_unit_in_consumer_units
            assortment_status AS assortment_status,
            -- , shelving_delay AS shelving_delay
            -- , legal_for_merchandising AS legal_for_merchandising
            -- , ilegal_for_merchandising AS ilegal_for_merchandising
            -- , reference_code AS reference_code
            -- , reference_location_code AS reference_location_code
            custom_nt AS custom_nt,
            custom_prevision_abierta AS custom_prevision_abierta
        FROM [dbo].[pub.md.product_locations];
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=[],
    #unique_combo=[],
    #domain_checks={},    #date_order=[],
)

#=================================
#     Sales prices  
#=================================
SALES_PRICES = InterfaceConfig(
    interface_name="sales_prices",
    source_sql="""
        SELECT
            product AS product,
            location AS location,
            start_date AS start_date,
            end_date AS end_date,
            sales_price AS sales_price,
            sales_price_with_vat AS sales_price_with_vat,
            price_type AS price_type,
            Igic AS Igic
        FROM [pub_md].[sales_prices]
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=["product", "location", "start_date"],
    #domain_checks={
    #    "state": ["", "DELETE"]
    #},
    date_order=[],
)

#=================================
#     Sales   
#=================================
SALES = InterfaceConfig(
    interface_name="sales",
    source_sql="""
        SELECT 
            receipt_timestamp AS receipt_timestamp,
            receipt_code AS receipt_code,
            date AS date,
            time AS time,
            location AS location,
            product AS product,
            Quantity AS quantity,
            receipt_row_number AS receipt_row_number,
            value AS value,
            sales_value_with_tax AS sales_value_with_tax,
            tax_amount AS tax_amount,
            sales_tax_rate AS sales_tax_rate,
            purchase_price AS purchase_price, 
            -- , campaign_code AS campaign_code
            -- , transaction_campaign_code AS transaction_campaign_code
            custom_supplier_cost AS custom_supplier_cost
            -- , loyalty_customer_type AS loyalty_customer_type
        FROM [pub_tx].[sales]
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=[],
    #domain_checks={
    #    "state": ["", "DELETE"]
    #},
    date_order=[],
)

#=================================
#   Promotions Competitor Prices   
#=================================
PROMOTIONS_COMPETITOR_PRICES = InterfaceConfig(
    interface_name="promotions_competitor_prices",
    source_sql="""
        SELECT
            observed_at AS observed_at,
            product AS product,
            competitor AS competitor,
            location AS location,
            location_attribute_name AS location_attribute_name,
            type AS type,
            sales_price AS sales_price
        FROM [pub_md].[promotions_competitor_prices]
    """,
    filename_date_fields=[],
    unique_id_mode="timestamp",
    required_non_null=[],
    #domain_checks={
    #    "state": ["", "DELETE"]
    #},
    date_order=[],
)

REGISTRY = {
    "product_groups": PRODUCT_GROUPS,
    "campaigns": CAMPAIGNS,
    "suppliers": SUPPLIERS,
    "products": PRODUCTS,
    "locations": LOCATIONS,
    "product_locations": PRODUCT_LOCATIONS,
    "sales_prices": SALES_PRICES,
    "sales": SALES,
    "promotions_competitor_prices": PROMOTIONS_COMPETITOR_PRICES,
}
