import pandas as pd
from bookstats.formatting import clean_whitespace

PUBLISHER_OVERRIDES = {
    "Simon Schuster": "Simon & Schuster",
    "W. W. Norton Company": "W. W. Norton & Company",
    "W.W. Norton & Company": "W. W. Norton & Company",
    "Ballantine": "Ballantine Books",
    "Bantam Books": "Bantam",
}

def publisher_dedup(col: pd.Series) -> pd.Series:
    """Creates key for multiple versions of same publisher, 
    then chooses most common version to apply and therefore deduplicate."""
    raw = col
    key = (raw
           .str.replace(r"\bPublishers?\b","", regex=True)
           .str.replace(r"\bLtd\.?(\s|$)","", regex=True)
           .str.replace(" & "," and "))
    key = clean_whitespace(key)
    
    # also targetting Simon Shuster specifically:
    key = key.str.replace("Simon Schuster", "Simon and Schuster")
    
    key = key.str.lower()
    
    # pick spelling based on frequency:
    d = pd.DataFrame({"raw": raw, "key": key})
    selected_values = d.groupby(key)["raw"].agg(lambda x: x.value_counts().idxmax())
    
    return key.map(selected_values)