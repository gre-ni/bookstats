import csv
from bookstats.config import RAW_DATA, RAW_DATA_EN

# Only keep books in English

books = []
with open(RAW_DATA, "r") as file: 
    reader = csv.DictReader(file)
    for book in reader:
        if book["language_code"] == "eng":
            books.append(book)


with open(RAW_DATA_EN, "w") as file: 
    writer = csv.DictWriter(file, fieldnames=books[0].keys())
    writer.writeheader()
    for book in books:
        writer.writerow(book)