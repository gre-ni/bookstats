import pytest
import pandas as pd
import numpy as np 
from bookstats.publishers import publisher_dedup

def test_and_dedup():
    col_before = pd.Series(["Mix and Max", "Mix and Max", "Mix & Max"])
    col_after = pd.Series(["Mix and Max", "Mix and Max", "Mix and Max"])
    pd.testing.assert_series_equal(publisher_dedup(col_before), col_after)

def test_ltd_dedup():
    col_before = pd.Series(["Mix and Max Ltd.", "Mix and Max Ltd", "Mix and Max Ltd", "Mix and Max"])
    col_after = pd.Series(["Mix and Max Ltd", "Mix and Max Ltd", "Mix and Max Ltd", "Mix and Max Ltd"])
    pd.testing.assert_series_equal(publisher_dedup(col_before), col_after)