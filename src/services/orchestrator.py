import pandas as pd
import os, csv
from src.config.interfaces import REGISTRY, InterfaceConfig
from src.repositories.product_groups_repository import ProductGroupsRepository
from src.repositories.suppliers_repository import SuppliersRepository
from src.repositories.campaigns_repository import CampaignsRepository
from src.repositories.products_repository import ProductsRepository
from src.repositories.locations_repository import LocationsRepository 
from src.repositories.sales_prices_repository import SalesPricesRepository
from src.repositories.product_locations_repository import ProductLocationsRepository
from src.repositories.sales_repository import SalesRepository
from src.repositories.promotions_competitor_prices_repository import PromotionsCompetitorPricesRepository
from src.mappers.product_groups_mapper import ProductGroupsMapper
from src.mappers.campaigns_mapper import CampaignsMapper
from src.mappers.suppliers_mapper import SuppliersMapper
from src.mappers.products_mapper import ProductsMapper 
from src.mappers.locations_mapper import LocationsMapper
from src.mappers.product_locations_mapper import ProductLocationsMapper
from src.mappers.sales_prices_mapper import SalesPricesMapper
from src.mappers.sales_mapper import SalesMapper
from src.mappers.promotions_competitor_prices_mapper import PromotionsCompetitorPricesMapper
from src.utils.csv_exporter import CsvExporter
from src.utils.export_config import ExportConfig
from src.services.validation_service import ValidationService
from src.services.file_namer import FileNamer

class Orchestrator:
    def run_interface(self, name: str) -> str:
        cfg: InterfaceConfig = REGISTRY[name]

        # 1) Repository → SPAR models
        if name == "product_groups":
            repo = ProductGroupsRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = ProductGroupsMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            # 2) a DataFrame para validaciones (y normalizaciones numéricas/fechas, si quieres)
            df = pd.DataFrame([x.model_dump() for x in relex_items])

            # 3) Validaciones estilo YAML (pero en Python)
            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            # 4) Nombre del fichero
            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            # 5) Export
            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            # ⚠️ Si no hay registros, exporta CSV vacío y termina
            if not relex_items:
                # CSV vacío (con cabecera) – también con tmp+rename si quieres igualarlo
                df_empty = pd.DataFrame(columns=df.columns)
                tmp_path = f"{out_path}.tmp"
                df_empty.to_csv(
                    tmp_path,
                    index=False,
                    sep=ExportConfig.DELIMITER,
                    encoding=ExportConfig.ENCODING,
                    header=True,
                    lineterminator=ExportConfig.LINE_TERMINATOR,
                    quoting=csv.QUOTE_ALL,
                    quotechar='"',
                    doublequote=True,
                )
                os.replace(tmp_path, out_path)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path
            
            # 6) Export normal con datos
            CsvExporter.export_to_csv(relex_items, out_path)
            return out_path
        
        elif name == "campaigns":
            repo = CampaignsRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = CampaignsMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path
        
        elif name == "suppliers":
            repo = SuppliersRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = SuppliersMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path

        elif name == "products":
            repo = ProductsRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = ProductsMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path
        
        elif name == "locations":
            repo = LocationsRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = LocationsMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path
        
        elif name == "product_locations":
            repo = ProductLocationsRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = ProductLocationsMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path
        
        elif name == "sales_prices":
            repo = SalesPricesRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = SalesPricesMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path
        
        elif name == "sales":
            repo = SalesRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = SalesMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path
        
        elif name == "promotions_competitor_prices":
            repo = PromotionsCompetitorPricesRepository(sql=cfg.source_sql)
            spar_items = repo.get_all()
            mapper = PromotionsCompetitorPricesMapper()
            relex_items = [mapper.map(x) for x in spar_items]

            df = pd.DataFrame([x.model_dump() for x in relex_items])

            ValidationService.validate_output(
                df,
                required_non_null=cfg.required_non_null,
                unique_combo=cfg.unique_combo,
                domain_checks=cfg.domain_checks,
                date_order=cfg.date_order,
            )

            filename = FileNamer.build_filename(
                interface_name=cfg.interface_name,
                df_out=df,
                filename_date_fields=cfg.filename_date_fields,
                unique_id_mode=cfg.unique_id_mode
            )

            out_path = f"{ExportConfig.OUTPUT_DIR}/{filename}"

            if not relex_items:
                df_empty = pd.DataFrame(columns=df.columns)
                df_empty.to_csv(out_path, 
                                index=False, 
                                sep=ExportConfig.DELIMITER,
                                lineterminator=ExportConfig.LINE_TERMINATOR,
                                encoding=ExportConfig.ENCODING, header=True)
                print(f"⚠️ No se recuperaron registros. CSV vacío generado en: {out_path}")
                return out_path

            CsvExporter.export_to_csv(relex_items, out_path)
            print(f"✅ Export completado: {out_path}")
            return out_path
        # elif name == "products": ...  # añades más casos con sus repo/mapper
        
        else:
            raise NotImplementedError(f"Interfaz no implementada: {name}")
        