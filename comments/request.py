import sqlite3
import json
from models import Comment

def get_all_comments():
    with sqlite3.connect("./picnic-fish.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.subject,
            c.created_on
        FROM comments c
        """)

        comments = []
        dataset = db_cursor.fetchall()
    
        for row in dataset:
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'], row['subject'], row['created_on'])
            comments.append(comment.__dict__)

    return json.dumps(comments)

def get_single_comment(id):
    with sqlite3.connect("./picnic-fish.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.subject,
            c.created_on
        FROM comments c
        WHERE c.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'], row['subject'], row['created_on'])

    return json.dumps(comment.__dict__)

def create_new_comment(new_comment):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Comments
            (post_id,
            author_id,
            content,
            subject,
            created_on)
        VALUES
            (?, ?, ?, ?, ?);
        """, (new_comment['post_id'], new_comment['author_id'], new_comment['content'], new_comment['subject'], new_comment['created_on'], ))

        id = db_cursor.lastrowid
        new_comment['id'] = id
    return json.dumps(new_comment)
