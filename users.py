from werkzeug.security import check_password_hash

import db

def create_user(username, password_hash):
    sql = "INSERT INTO Users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    if len(username) < 4 or len(username) > 16:
        return None
    sql = "SELECT id, password_hash FROM Users WHERE username = ?"
    result = db.query(sql, [username])
    if not result:
        return None
    else:
        result = result[0]
    user_id = result["id"]
    password_hash = result["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
    else:
        return None

def get_user(user_id):
    sql = """SELECT id, username
                FROM Users
                WHERE id = ?"""
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_collection(user_id, page, page_size):
    sql = """SELECT id,
                    title,
                    artist,
                    comment
                FROM Entries
                WHERE user_id = ?
                ORDER BY id DESC
                LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [user_id, limit, offset])