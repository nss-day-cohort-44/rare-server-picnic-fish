import sqlite3
import json
from models import Post

def get_all_posts():

    with sqlite3.connect("./picnic-fish.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
        """)

        posts = []

        dataset = db_cursor.fetchall()
        for row in dataset:
            post = Post(row['userId'], row['categoryId'], row["title"], row["publicationDate"],
                            row['imageUrl'], row['content'], row['approved'])
            posts.append(post.__dict__)

    return json.dumps(posts)

def get_single_post():
    with sqlite3.connect("./picnic-fish.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
            """, (id, ))

            data = db_cursor.fetchone()

            post = Post(data['id'], data['userId'], data['categoryId'], data["title"], data["publicationDate"],
                            data['imageUrl'], data['content'], data['approved'])
            return json.dumps(post.__dict__)

def create_post(new_post):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO posts
            (id, userId, categoryId, title, publicationDate,
            imageUrl, content, approved)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?);
        """, ((new_post['id'], new_post['userId'], new_post['categoryId'], new_post["title"], new_post["publicationDate"],
                            new_post['imageUrl'], new_post['content'], new_post['approved'], )))
    return json.dumps(new_post)