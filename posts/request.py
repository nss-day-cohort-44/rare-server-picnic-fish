import sqlite3
import json
from models import Post
from models.user import User
from models.categories import Category

def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./picnic-fish.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.password,
            u.bio,
            u.username,
            u.profile_image_url,
            u.created_on,
            u.active,
            u.account_type_id,
            c.label
        FROM posts p
        JOIN users u
            ON u.id = p.user_id
        JOIN categories c
            ON c.id = p.category_id
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            post = Post(row['user_id'], row['category_id'], row["title"], row["publication_date"], row['image_url'], row['content'], row['approved'])

            user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                        row['password'], row['bio'], row['username'], row['profile_image_url'], row['created_on'],
                        row['active'], row['account_type_id'])
            post.user = user.__dict__

            category = Category(row['id'], row['label'])
            post.category = category.__dict__

            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)