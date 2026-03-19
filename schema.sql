CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE Entries (
    id INTEGER PRIMARY KEY,
    title TEXT,
    artist TEXT,
    comment TEXT,
    user_id INTEGER REFERENCES Users
);