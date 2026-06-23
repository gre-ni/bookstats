import csv
import re

def clean_string(string: str) -> str:
    return string.strip().replace("  ", " ")