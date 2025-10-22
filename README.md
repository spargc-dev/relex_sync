# SPAR to RELEX Sync

This project provides a synchronization tool to transform SPAR entities into RELEX domain entities.

## Project Structure

```
src/
├── models/
│   ├── spar_models.py     # SPAR domain models
│   └── relex_models.py    # RELEX domain models
├── mappers/
│   └── product_mapper.py  # Mapper for converting between models
├── utils/
│   └── csv_exporter.py    # Utility for CSV export
└── main.py               # Main synchronization script
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install pydantic pandas python-dotenv
```

3. Create a `.env` file in the project root with:
```
OUTPUT_DIR=output
```

## Usage

Run the synchronization script:

```bash
python src/main.py
```

The script will:
1. Fetch products from SPAR system
2. Transform them to RELEX format
3. Export them to a CSV file in the configured output directory

## Models

### SPAR Product
- `product_id`: String (must start with 'SP')
- `name`: String
- `description`: Optional string
- `price`: Decimal (non-negative)
- `stock`: Integer (non-negative)
- `category`: String
- `last_updated`: DateTime

### RELEX Product
- `relex_id`: String (must start with 'RX')
- `product_name`: String
- `product_description`: Optional string
- `unit_price`: Decimal (non-negative)
- `available_quantity`: Integer (non-negative)
- `product_category`: String
- `update_timestamp`: DateTime

## Business Rules

Both models include validation rules:
- IDs must follow specific formats (SP for SPAR, RX for RELEX)
- Prices cannot be negative
- Stock/quantity cannot be negative

## Output

The script generates CSV files in the configured output directory with the format:
`relex_products_YYYYMMDD_HHMMSS.csv`