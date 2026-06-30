from bookstats.config import RAW_DATA, FILTERED_DATA
from bookstats.utils import SUPPORTED_LANGUAGE_CODES
import pandas as pd

df = pd.read_csv(RAW_DATA, on_bad_lines='warn')

# Masks
is_language = df["language_code"].isin(SUPPORTED_LANGUAGE_CODES)
is_book = df["authors"] != "NOT A BOOK"
is_not_set = ~df["title"].str.contains(r"#\d-\d", regex=True)

# Filter by language:
df = df[is_language]
df = df[is_book]
df = df[is_not_set]


df.to_csv(FILTERED_DATA, index=False)