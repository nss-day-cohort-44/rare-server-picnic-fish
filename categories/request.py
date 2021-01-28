import sqlite3
import json
from models import Category

def get_all_categories():

    with sqlite3.connect("./picnic-fish.db") as conn:
                conn.row_factory = sqlite3.Row
                db_cursor = conn.cursor()

                db_cursor.execute("""
                SELECT
                    c.id,
                    c.label
                FROM categories c
                """)

                categories =[]
                dataset = db_cursor.fetchall()
            
                for row in dataset:
                    category = Category(row['id'],row['label'])

                    categories.append(category.__dict__)

                return json.dumps(categories)

def get_single_category(id):
    with sqlite3.connect("./picnic-fish.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                c.id,
                c.label
            FROM categories c
            WHERE c.id = ?
            """, (id,))

            data = db_cursor.fetchone()

            category = Category(data['id'],data['label'])

            return json.dumps(category.__dict__)

def create_category(new_category):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO categories
            ('label')
        VALUES
            (?);
        """, (new_category['label']))

        id = db_cursor.lastrowid
        new_category['id'] = id
    return json.dumps(new_category)




