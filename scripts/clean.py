from bookstats.formatting import clean_whitespace, clean_headers
from bookstats.publishers import publisher_dedup, PUBLISHER_OVERRIDES
from bookstats.config import FILTERED_DATA, CLEAN_DATA
import pandas as pd
import numpy as np

df = pd.read_csv(FILTERED_DATA)

# Clean headers:
clean_headers(df)

# Clean whitespace on string columns:
df["authors"] = clean_whitespace(df["authors"])
df["title"] = clean_whitespace(df["title"])
df["publisher"] = clean_whitespace(df["publisher"])

# Formatting fixes on string columns:
df["title"] = df["title"].str.replace(" : ", ": ")

# Replace 0 to NaN on page count:
df["num_pages"] = df["num_pages"].replace(0, np.nan)

# 0 to NaN on ratings_count with non-zero average:
has_unrated_avg = (df["average_rating"] != 0) & (df["ratings_count"] == 0)
df["ratings_count"] = df["ratings_count"].mask(has_unrated_avg)

# Publisher-specific cleanup, generic and targeted:
df["publisher"] = publisher_dedup(df["publisher"])
df["publisher"] = df["publisher"].replace(PUBLISHER_OVERRIDES)

# Change of date format to ISO
df["publication_date"] = pd.to_datetime(df["publication_date"], format="%m/%d/%Y", errors="coerce").dt.strftime("%Y-%m-%d")

df.to_csv(CLEAN_DATA, index=False)


