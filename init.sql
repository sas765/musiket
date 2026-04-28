DELETE FROM Classes;

INSERT INTO Classes (title, value) VALUES ("Type", "Album");
INSERT INTO Classes (title, value) VALUES ("Type", "Single");
INSERT INTO Classes (title, value) VALUES ("Type", "EP");
INSERT INTO Classes (title, value) VALUES ("Type", "Compilation");
INSERT INTO Classes (title, value) VALUES ("Type", "Mixtape");

INSERT INTO Classes (title, value) VALUES ("Format", "CD");
INSERT INTO Classes (title, value) VALUES ("Format", "Cassette");
INSERT INTO Classes (title, value) VALUES ("Format", "Vinyl");
INSERT INTO Classes (title, value) VALUES ("Format", "Digital");

INSERT INTO Sort_options (name, value) VALUES ("newest", "e.id");
INSERT INTO Sort_options (name, value) VALUES ("title", "e.title");
INSERT INTO Sort_options (name, value) VALUES ("artist", "e.artist");
INSERT INTO Sort_options (name, value) VALUES ("username", "u.username");