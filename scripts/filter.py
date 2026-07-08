from bookstats.config import RAW_DATA, FILTERED_DATA
from bookstats.utils import SUPPORTED_LANGUAGE_CODES
import pandas as pd

df = pd.read_csv(RAW_DATA, on_bad_lines='warn')

# Masks
is_language = df["language_code"].isin(SUPPORTED_LANGUAGE_CODES)
is_book = df["authors"] != "NOT A BOOK"
is_not_set = ~df["title"].str.contains(r"#\d-\d", regex=True)

# Filter all:
keep = is_language & is_book & is_not_set
df = df[keep]

df = df.reset_index(drop=True)


df.to_csv(FILTERED_DATA, index=False)

# TODO: