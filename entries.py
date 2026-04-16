import db

def new_entry(title, artist, comment, user_id, classes):
    sql = """INSERT INTO Entries (title, artist, comment, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, artist, comment, user_id])

    entry_id = db.last_insert_id()

    sql = """INSERT INTO Entry_classes (entry_id, title, value)
                VALUES (?, ?, ?)"""
    for title, value in classes:
        db.execute(sql, [entry_id, title, value])

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

def find_entries(query):
    sql = """SELECT e.id, e.title, e.artist, u.username, e.user_id
                FROM Entries e, Users u
                WHERE u.id = e.user_id
                AND (e.title LIKE ?
                OR e.artist LIKE ?
                OR e.comment LIKE ?
                OR u.username LIKE ?)
                ORDER BY e.id DESC"""
    return db.query(sql, ["%" + query + "%"] * 4)

def get_entries():
    sql = """SELECT e.id, e.title, e.artist, e.user_id, u.username
                FROM Entries e, Users u
                WHERE u.id = e.user_id
                ORDER BY e.id DESC"""
    return db.query(sql)

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
    for title, value in classes:
        db.execute(sql, [entry_id, title, value])

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