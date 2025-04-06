CREATE TABLE artists (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists (id)
);

CREATE TABLE songs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    duration INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES albums (id)
);