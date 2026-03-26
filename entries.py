import db

def new_entry(title, artist, comment, user_id):
    sql = """INSERT INTO Entries (title, artist, comment, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, artist, comment, user_id])

def get_entries():
    sql = """SELECT e.id, e.title, e.artist, u.username
                FROM Entries e, Users u
                WHERE u.id = e.user_id
                ORDER BY e.id DESC"""
    return db.query(sql)

def get_entry(entry_id):
    sql = """SELECT e.title, e.artist, e.comment, u.username
                FROM Entries e, Users u
                WHERE u.id = e.user_id AND e.id = ?"""
    return db.query(sql, [entry_id])[0]