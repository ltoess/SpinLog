CREATE TABLE Artist (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Release (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT NOT NULL, 
    artist_id INTEGER NOT NULL,
    year INTEGER,
    format TEXT, 
    CONSTRAINT fk_release_artist
        FOREIGN KEY (artist_id)
        REFERENCES Artist(id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE Pressing (
    id INTEGER PRIMARY KEY AUTO_INCREMENT, 
    release_id INTEGER NOT NULL, 
    year INTEGER, 
    format TEXT, 
    CONSTRAINT fk_pressing_release
        FOREIGN KEY (release_id)
        REFERENCES Release(id)
        ON DELETE NO ACTION 
        ON UPDATE NO ACTION    
);

CREATE TABLE Spin (
    id INTEGER PRIMARY KEY AUTO_INCREMENT 
    pressing_id INTEGER NOT NULL 
    played_at DATETIME 
    note TEXT
    CONSTRAINT fk_spin_pressing
        FOREIGN KEY (pressing_id)
        REFERENCES Pressing(id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);
