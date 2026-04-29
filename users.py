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
    result = result[0]
    user_id = result["id"]
    password_hash = result["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
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

def count_messages(user_id):
    sql = """SELECT IFNULL(COUNT(m.id), 0) messages,
                    IFNULL(COUNT(DISTINCT e.id), 0) entries
                FROM Messages m, Entries e
                WHERE m.entry_id = e.id
                AND m.user_id = ?"""
    return db.query(sql, [user_id])[0]

def get_discussed_entries(user_id, page, page_size):
    sql = """SELECT DISTINCT e.id FROM Messages m, Entries e
                WHERE m.entry_id = e.id
                AND m.user_id = ?
                ORDER BY m.id DESC"""
    id_result = db.query(sql, [user_id])

    offset = page_size * (page - 1)
    limit = page_size + offset

    sql = """SELECT e.id,
                    e.title,
                    e.artist,
                    e.user_id,
                    u.username
                FROM Entries e, Users u
                WHERE e.id = ?
                AND u.id = e.user_id"""
    result = []
    for entry_id in id_result:
        result.append(db.query(sql, [entry_id[0]])[0])
    return result[offset:limit]
