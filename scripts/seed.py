import sqlite3
import csv
from pathlib import Path 

DB_PATH = Path(__file__).parent.parent / "data"
con = sqlite3.connect(DB_PATH) 

with open("../data/raw/books.csv", "r") as f:
    db = con.cursor()
    db.execute(""""
               
               """)