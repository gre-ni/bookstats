DROP TABLE IF EXISTS "books_authors";
DROP TABLE IF EXISTS "books";
DROP TABLE IF EXISTS "authors";
DROP TABLE IF EXISTS "series";
DROP TABLE IF EXISTS "publishers";


CREATE TABLE "publishers" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id")
);

CREATE TABLE "series" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id")
);

CREATE TABLE "authors" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id")
);

CREATE TABLE "books" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "publisher_id" INTEGER NOT NULL,
    "publication_date" TEXT,
    "series_id" INTEGER,
    "series_part" INTEGER,
    "isbn" TEXT UNIQUE,
    "isbn13" TEXT UNIQUE,
    "average_rating" REAL,
    "ratings_count" INTEGER,
    "text_reviews_count" INTEGER,
    "num_pages" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("publisher_id") REFERENCES "publishers"("id"),
    FOREIGN KEY("series_id") REFERENCES "series"("id")
);

CREATE TABLE "books_authors" (
    "book_id" INTEGER,
    "author_id" INTEGER,
    PRIMARY KEY("book_id", "author_id"),
    FOREIGN KEY("book_id") REFERENCES "books"("id"),
    FOREIGN KEY("author_id") REFERENCES "authors"("id")    
);