import sqlite3
import json
from models import PostTag


def get_all_post_tags():

    with sqlite3.connect("./picnic-fish.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id

        FROM PostTags pt
            """)

        post_tags = []
 
        dataset = db_cursor.fetchall()

        for row in dataset:

            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'])

            post_tags.append(post_tag.__dict__)

        return json.dumps(post_tags)


def create_post_tag(post_tag_list):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()
        dataset = []
        

        for post_tag in post_tag_list:
            db_cursor.execute("""
            INSERT INTO posttags
                (post_id , tag_id)
                VALUES (? , ?);
            """,
            (post_tag['postId'], post_tag['id'], ))

            id = db_cursor.lastrowid
            post_tag['ptid'] = id

            dataset.append(post_tag)

    return json.dumps(dataset)
