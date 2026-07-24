from bookstats.config import RAW_DATA, FILTERED_DATA
from bookstats.utils import SUPPORTED_LANGUAGE_CODES
import pandas as pd


def filter_books(df: pd.DataFrame) -> pd.DataFrame:
    """Drops rows for unwanted language, drops box sets, drops titles with 'NOT A BOOK' authors."""
    is_language = df["language_code"].isin(SUPPORTED_LANGUAGE_CODES)
    is_book = df["authors"] != "NOT A BOOK"
    is_not_set = ~df["title"].str.contains(r"#\d-\d", regex=True)

    keep = is_language & is_book & is_not_set
    
    return df[keep]

def main():
    df = pd.read_csv(RAW_DATA, on_bad_lines='warn')
    df = filter_books(df)

    df = df.reset_index(drop=True)
    df.to_csv(FILTERED_DATA, index=False)
    print("Filtering complete.")

if __name__ == "__main__":
    main()