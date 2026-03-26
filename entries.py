import db

def new_entry(title, artist, comment, user_id):
    sql = """INSERT INTO Entries (title, artist, comment, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, artist, comment, user_id])
