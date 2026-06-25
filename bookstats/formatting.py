# Functions for string formatting purposes
import re
import pandas as pd

def clean_whitespace(col: pd.Series) -> pd.Series:
    """Strip leading/trailing and collapse whitespace in a string Series."""
    col = col.str.strip()
    col = col.str.replace(r" {2,}"," ",regex=True)
    return col

