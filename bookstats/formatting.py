# Functions for string formatting purposes
import re
import pandas as pd

def clean_string(col: pd.Series) -> pd.Series:
    return col.str.strip()