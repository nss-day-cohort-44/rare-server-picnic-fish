import sqlite3
import json
from models import User, accountTypes

def get_all_users():

    with sqlite3.connect("./picnic-fish.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
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
            a.id a_id,
            a.label

        FROM User u
        JOIN AccountTypes a
            ON u.account_type_id = a.a_id
        WHERE u.id              
        """)

        users =[]

        dataset = db_cursor.fetchall()

        for row in dataset:

            user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                    row['password'], row['bio'], row['username'], row['profile_image_url'],
                    row['created_on'], row['active'], row['account_type_id'])

            accountType = accountTypes(row['id'], row['label'])

            user.accountType = accountType.__dict__ 

            users.append(user.__dict__) 

    return json.dumps(users)  