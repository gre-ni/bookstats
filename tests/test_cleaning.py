import pytest
import pandas as pd
import numpy as np 
from bookstats.formatting import clean_whitespace


@pytest.mark.parametrize("raw, expected", [
    ("Jane  Austen",     "Jane Austen"),
    ("  Jane Austen  ",   "Jane Austen"),
    ("Jane     Austen",  "Jane Austen"),
    ("no change", "no change"),
    ("", ""),
])
def test_clean_whitespace(raw, expected):
    """Happy path"""
    col_before = pd.Series([raw])
    col_after = pd.Series([expected])
    pd.testing.assert_series_equal(clean_whitespace(col_before), col_after)
    
def test_clean_whitespace_error():
    """Exception on NaN dtype Series"""
    col_null = pd.Series([np.nan])
    with pytest.raises(AttributeError):
        clean_whitespace(col_null)

def test_clean_whitespace_mixed():
    """NaN in string Series gets skipped"""
    col_mixed_before = pd.Series(["Jane  Austen", np.nan, "Mark  Twain"])
    col_mixed_after = pd.Series(["Jane Austen", np.nan, "Mark Twain"])
    pd.testing.assert_series_equal(clean_whitespace(col_mixed_before), col_mixed_after)