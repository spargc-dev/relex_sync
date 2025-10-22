import pandas as pd

class ValidationService:
    @staticmethod
    def validate_output(df: pd.DataFrame,
                        required_non_null: list[str] = None,
                        unique_combo: list[list[str]] = None,
                        domain_checks: dict = None,
                        date_order: list[tuple[str,str]] = None) -> None:
        required_non_null = required_non_null or []
        unique_combo = unique_combo or []
        domain_checks = domain_checks or {}
        date_order = date_order or []

        errs = []

        for c in required_non_null:
            if c not in df.columns:
                errs.append(f"Columna requerida no existe: {c}")
            else:
                if df[c].isna().any() or (df[c].astype(str).str.len()==0).any():
                    errs.append(f"Nulos/vacíos en requerido: {c}")

        for combo in unique_combo:
            missing = [c for c in combo if c not in df.columns]
            if missing:
                errs.append(f"Unique combo referencia columnas inexistentes: {missing}")
                continue
            dup = df.duplicated(subset=combo, keep=False)
            if dup.any():
                sample = df.loc[dup, combo].head(5).to_dict(orient="records")
                errs.append(f"Duplicados clave {combo}: {sample}")

        for c, allowed in (domain_checks or {}).items():
            if c in df.columns:
                bad = ~df[c].isin(allowed)
                if bad.any():
                    errs.append(f"Fuera de dominio en {c}: {df.loc[bad, c].unique()[:10]}")

        for a, b in (date_order or []):
            if a in df.columns and b in df.columns:
                aa = pd.to_datetime(df[a], errors="coerce")
                bb = pd.to_datetime(df[b], errors="coerce")
                bad = (aa > bb) & aa.notna() & bb.notna()
                if bad.any():
                    errs.append(f"Fechas incoherentes {a}>{b} en {bad.sum()} filas")

        if errs:
            raise ValueError("Validaciones RELEX fallidas: " + " | ".join(map(str, errs)))
