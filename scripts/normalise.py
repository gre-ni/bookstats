import pandas as pd
from bookstats.config import CLEAN_DATA, MODELLED_DATA
from bookstats.formatting import clean_whitespace

SERIES_PATTERN = r" \(([^#()]+) \#(\d+)\)"

def separate_series(title: pd.Series, pattern=SERIES_PATTERN) -> tuple[pd.Series, pd.Series]:
    """Extracts series name and number from title column and return column tuple of (series, number) in that order"""
    extracted = title.str.extract(pattern)
    return extracted.iloc[:,0], extracted.iloc[:,1]

def clean_series_title(title: pd.Series, pattern=SERIES_PATTERN) -> pd.Series:
    """Strips away series information from book title"""
    title = title.str.replace(pattern, "", regex=True)
    return title

def author_split(authors: pd.Series) -> pd.Series:
    """Splitting multiple authors based on /"""
    return authors.str.split("/")

def normalise_books(df: pd.DataFrame) -> pd.DataFrame:
    """Apply normalisation steps: series split, authors fan out."""
    # Splitting series and cleaning titles
    df["series_name"], df["series_part"] = separate_series(df["title"])
    df["title"] = clean_series_title(df["title"])

    # Split authors and explode + whitespace clean
    df["authors"] = author_split(df["authors"])

    df = df.explode("authors")
    df["authors"] = clean_whitespace(df["authors"])
    
    return df

def main():
    df = pd.read_csv(CLEAN_DATA)
    df = normalise_books(df)

    df.to_csv(MODELLED_DATA, index=False)
    print("Modelling complete.")

if __name__ == "__main__":
    main()

