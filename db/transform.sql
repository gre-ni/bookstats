INSERT INTO authors ("name")
SELECT DISTINCT "authors" FROM staging;

INSERT INTO publishers ("name")
SELECT DISTINCT "publisher" FROM staging;

INSERT INTO series ("name") 
SELECT DISTINCT "series_name" FROM staging
WHERE staging.series_name IS NOT NULL;

INSERT INTO books ("title", "publisher_id", "publication_date", 
"series_id", "series_part", 
"isbn", "isbn13", 
"average_rating", "ratings_count", "text_reviews_count", 
"num_pages")
SELECT DISTINCT staging.title, --title
    (SELECT id FROM publishers WHERE publishers.name = staging.publisher), -- publisher_id
staging.publication_date,
    (SELECT id FROM series WHERE series.name = staging.series_name), -- series_id
CAST(series_part AS INTEGER),
staging.isbn,
staging.isbn13, -- isbn13
staging.average_rating, --average_rating
CAST(staging.ratings_count AS INTEGER),
CAST(staging.text_reviews_count AS INTEGER),
CAST(staging.num_pages AS INTEGER)
FROM staging;

INSERT INTO books_authors ("book_id", "author_id")
SELECT DISTINCT books.id, authors.id 
FROM staging
JOIN books ON books.isbn = staging.isbn
JOIN authors ON authors.name = staging.authors;
