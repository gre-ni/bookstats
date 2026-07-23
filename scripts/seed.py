import sqlite3
import pandas as pd
from bookstats.config import DB_PATH, SCHEMA, TRANSFORM, MODELLED_DATA


with sqlite3.connect(DB_PATH) as con:

    con.execute("PRAGMA foreign_keys = ON")

    pd.read_csv(MODELLED_DATA).to_sql("staging", con, index=False, if_exists='replace')

    con.executescript(SCHEMA.read_text())
    con.executescript(TRANSFORM.read_text())

    con.execute("DROP TABLE staging")

con.close()