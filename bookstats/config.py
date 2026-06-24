from pathlib import Path 

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DATA = DATA_DIR / "raw" / "books.csv"
PUBLISHERS = DATA_DIR / "interim" / "publishers.csv"
RAW_DATA_EN = DATA_DIR / "interim" / "books_english.csv"
CLEAN_DATA = DATA_DIR / "clean" / "books_clean.csv"
DB_PATH = ROOT_DIR / "db" / "books.db"