CREATE TABLE Artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL, 
    artist_id INTEGER NOT NULL,
    year INTEGER,
    record_format TEXT, 
    CONSTRAINT fk_album_artist
        FOREIGN KEY (artist_id)
        REFERENCES Artist(id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
    CONSTRAINT uq_album UNIQUE (title, artist_id)
);

CREATE TABLE Pressing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    album_id INTEGER NOT NULL,
    catalog_number TEXT,
    year INTEGER,
    format TEXT,
    CONSTRAINT fk_pressing_album
        FOREIGN KEY (album_id)
        REFERENCES Album(id)
        ON DELETE NO ACTION 
        ON UPDATE NO ACTION
);

CREATE TABLE Spin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pressing_id INTEGER NOT NULL,
    played_at DATETIME,
    note TEXT,
    CONSTRAINT fk_spin_pressing
        FOREIGN KEY (pressing_id)
        REFERENCES Pressing(id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);
