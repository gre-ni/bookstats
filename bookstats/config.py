from pathlib import Path 

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DATA = DATA_DIR / "raw" / "books.csv"
FILTERED_DATA = DATA_DIR / "interim" / "books_filtered.csv"
CLEAN_DATA = DATA_DIR / "clean" / "books_clean.csv"
MODELLED_DATA = DATA_DIR / "clean" / "books_modelled.csv"
DB_PATH = ROOT_DIR / "db" / "books.db"
SCHEMA = ROOT_DIR / "db" / "schema.sql"
TRANSFORM = ROOT_DIR / "db" / "transform.sql"