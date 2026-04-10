import db

def new_entry(title, artist, comment, user_id):
    sql = """INSERT INTO Entries (title, artist, comment, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, artist, comment, user_id])

def find_entries(query):
    sql = """SELECT e.id, e.title, e.artist, u.username
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

def update_entry(title, artist, comment, entry_id):
    sql = """UPDATE Entries SET title = ?,
                                artist = ?,
                                comment = ?
                            WHERE id = ?"""
    db.execute(sql, [title, artist, comment, entry_id])

def remove_entry(entry_id):
    sql = "DELETE FROM Entries WHERE id = ?"
    db.execute(sql, [entry_id])