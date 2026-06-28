# Functions for string formatting purposes
import re
import pandas as pd

def clean_whitespace(col: pd.Series) -> pd.Series:
    """Strip leading/trailing and collapse whitespace in a string Series."""
    col = col.str.strip()
    col = col.str.replace(r" {2,}"," ",regex=True)
    return col

def clean_headers(df: pd.DataFrame) -> None:
    """Cleaning header of passed in DataFrame, direct adjustment."""
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r" {2,}"," ",regex=True)