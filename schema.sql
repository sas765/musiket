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

CREATE TABLE Entry_classes (
    id INTEGER PRIMARY KEY,
    entry_id INTEGER REFERENCES Entries,
    title TEXT,
    value TEXT
);

CREATE TABLE Classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE Messages (
    id INTEGER PRIMARY KEY,
    content TEXT,
    sent_at TEXT,
    user_id INTEGER REFERENCES Users,
    entry_id INTEGER REFERENCES Entries
);

CREATE TABLE Images (
    id INTEGER PRIMARY KEY,
    entry_id INTEGER REFERENCES Entries,
    image BLOB,
    alt TEXT
);

CREATE INDEX idx_entry_user ON Entries (user_id);
CREATE INDEX idx_message_user ON Messages (user_id);
CREATE INDEX idx_message_entry ON Messages (entry_id);