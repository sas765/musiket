import db

def new_entry(title, artist, comment, user_id, classes):
    sql = """INSERT INTO Entries (title, artist, comment, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, artist, comment, user_id])

    entry_id = db.last_insert_id()

    sql = """INSERT INTO Entry_classes (entry_id, title, value)
                VALUES (?, ?, ?)"""
    for c_title, c_value in classes:
        db.execute(sql, [entry_id, c_title, c_value])

def get_all_classes():
    sql = "SELECT title, value FROM Classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        if title not in classes:
            classes[title] = []
        classes[title].append(value)

    return classes

def get_classes(entry_id):
    sql = """SELECT title, value FROM Entry_classes
                WHERE entry_id = ?"""
    return db.query(sql, [entry_id])

def find_entries(query, order, page, page_size):
    if order == "0":
        sql = """SELECT e.id, e.title, e.artist, u.username, e.user_id
                    FROM Entries e, Users u
                    WHERE u.id = e.user_id
                    AND (e.title LIKE ?
                    OR e.artist LIKE ?
                    OR e.comment LIKE ?
                    OR u.username LIKE ?)
                    ORDER BY e.id DESC
                    LIMIT ? OFFSET ?"""
    else:
        sql = """SELECT e.id, e.title, e.artist, u.username, e.user_id
                    FROM Entries e, Users u
                    WHERE u.id = e.user_id
                    AND (e.title LIKE ?
                    OR e.artist LIKE ?
                    OR e.comment LIKE ?
                    OR u.username LIKE ?)
                    ORDER BY e.id ASC
                    LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, ["%" + str(query) + "%"] * 4 + [limit, offset])

def count_results(query, order):
    if order == "0":
        sql = """SELECT IFNULL(COUNT(e.id), 0) result
                    FROM Entries e, Users u
                    WHERE u.id = e.user_id
                    AND (e.title LIKE ?
                    OR e.artist LIKE ?
                    OR e.comment LIKE ?
                    OR u.username LIKE ?)
                    ORDER BY e.id DESC"""
    else:
        sql = """SELECT IFNULL(COUNT(e.id), 0) result
                    FROM Entries e, Users u
                    WHERE u.id = e.user_id
                    AND (e.title LIKE ?
                    OR e.artist LIKE ?
                    OR e.comment LIKE ?
                    OR u.username LIKE ?)
                    ORDER BY e.id ASC"""
    return db.query(sql, ["%" + str(query) + "%"] * 4)[0]["result"]

def count_entries(user_id="%"):
    sql = """SELECT COUNT(id) result FROM Entries
                WHERE user_id LIKE ?"""
    return db.query(sql, [user_id])[0]["result"]

def get_entries(page, page_size):
    sql = """SELECT e.id, e.title, e.artist, e.user_id, u.username
                FROM Entries e, Users u
                WHERE u.id = e.user_id
                ORDER BY e.id DESC
                LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

def get_entry(entry_id):
    sql = """SELECT e.id,
                    e.title,
                    e.artist,
                    e.comment,
                    u.username,
                    u.id user_id
                FROM Entries e, Users u
                WHERE u.id = e.user_id AND e.id = ?"""
    result = db.query(sql, [entry_id])
    return result[0] if result else None

def update_entry(title, artist, comment, entry_id, classes):
    sql = """UPDATE Entries SET title = ?,
                                artist = ?,
                                comment = ?
                            WHERE id = ?"""
    db.execute(sql, [title, artist, comment, entry_id])

    sql = "DELETE FROM Entry_classes WHERE entry_id = ?"
    db.execute(sql, [entry_id])

    sql = """INSERT INTO Entry_classes (entry_id, title, value)
                VALUES (?, ?, ?)"""
    for c_title, c_value in classes:
        db.execute(sql, [entry_id, c_title, c_value])

def remove_entry(entry_id):
    sql = "DELETE FROM Entry_classes WHERE entry_id = ?"
    db.execute(sql, [entry_id])
    sql = "DELETE FROM Entries WHERE id = ?"
    db.execute(sql, [entry_id])

def get_discussion(entry_id):
    sql = """SELECT m.id, m.content, m.sent_at, m.user_id, u.username
                FROM Messages m, Users u
                WHERE m.entry_id = ?
                AND m.user_id = u.id
                ORDER BY m.id"""
    return db.query(sql, [entry_id])

def get_message(message_id):
    sql = """SELECT m.id, m.content, m.sent_at, m.user_id, m.entry_id, u.username
                FROM Messages m, Users u
                WHERE m.id = ?
                AND u.id = m.user_id"""
    return db.query(sql, [message_id])[0]

def add_message(content, user_id, entry_id):
    sql = """INSERT INTO Messages (content, sent_at, user_id, entry_id)
             VALUES (?, datetime('now'), ?, ?)"""
    db.execute(sql, [content, user_id, entry_id])

def update_message(message_id, content):
    sql = "UPDATE Messages SET content = ? WHERE id = ?"
    db.execute(sql, [content, message_id])

def remove_message(message_id):
    sql = "DELETE FROM Messages WHERE id = ?"
    db.execute(sql, [message_id])

def add_image(entry_id, image, alt):
    sql = """INSERT INTO Images (entry_id, image, alt)
                VALUES (?, ?, ?)"""
    db.execute(sql, [entry_id, image, alt])

def get_image(image_id):
    sql = """SELECT image, alt FROM Images
                WHERE id = ?"""
    return db.query(sql, [image_id])

def update_image(entry_id, image):
    sql = "UPDATE users SET image = ? WHERE id = ?"
    db.execute(sql, [image, entry_id])

def remove_image(entry_id, image_id):
    sql = "DELETE FROM Images WHERE id = ? AND entry_id = ?"
    db.execute(sql, [image_id, entry_id])

def get_images(entry_id):
    sql = """SELECT id, alt FROM Images
                WHERE entry_id = ?"""
    return db.query(sql, [entry_id])
