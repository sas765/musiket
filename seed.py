import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM Users")
db.execute("DELETE FROM Entries")
db.execute("DELETE FROM Messages")

user_count = 1000
entry_count = 10**6
message_count = 10**7

for i in range(1, user_count + 1):
    db.execute("INSERT INTO Users (username, password_hash) VALUES (?, 'password')",
               ["user" + str(i)])

for i in range(1, entry_count + 1):
    db.execute("INSERT INTO Entries (title, artist, comment, user_id) VALUES (?, ?, ?, ?)",
               ["entry" + str(i), str(i) + "artist", str(i), random.randint(1, user_count)])

for i in range(1, message_count + 1):
    user_id = random.randint(1, user_count)
    entry_id = random.randint(1, entry_count)
    db.execute("""INSERT INTO Messages (content, sent_at, user_id, entry_id)
                  VALUES (?, datetime('now'), ?, ?)""",
               ["message" + str(i), user_id, entry_id])

db.commit()
db.close()