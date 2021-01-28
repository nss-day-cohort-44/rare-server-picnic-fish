import sqlite3
import json
from models import Comment

def create_new_comment(new_comment):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            (content, subject)
        VALUES
            (?, ?);
        """, (new_comment['content'], new_comment['subject'], ))

        id = db_cursor.lastrowid
        new_comment['id'] = id
    return json.dumps(new_comment)
