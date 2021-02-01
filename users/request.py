import sqlite3
import json
from models import User 
from models import AccountType

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

        FROM Users u
        JOIN AccountTypes a
            ON u.account_type_id = a.id
        WHERE u.id              
        """)

        users =[]

        dataset = db_cursor.fetchall()

        for row in dataset:

            user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                    row['password'], row['bio'], row['username'], row['profile_image_url'],
                    row['created_on'], row['active'], row['account_type_id'])

            accountType = AccountType(row['id'], row['label'])

            user.accountType = accountType.__dict__ 

            users.append(user.__dict__) 

        return json.dumps(users)  


def get_single_user(id):

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
        WHERE u.id = ?             
        """, (id, ))


        data = db_cursor.fetchone() 

        user = User(data['id'], data['first_name'], data['last_name'], data['email'],
                    data['password'], data['bio'], data['username'], data['profile_image_url'],
                    data['created_on'], data['active'], data['account_type_id'])

        accountType = AccountType(data['id'], data['label'])

        user.accountType = accountType.__dict__ 

        return json.dumps(user.__dict__) 


def create_user(new_user):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Users (
            'first_name', 
            'last_name', 
            'email', 
            'password', 
            'bio', 
            'username',
            'profile_image_url',
            'created_on', 
            'active',
            'account_type_id') 
            VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);   
        """, (new_user['firstName'], 
            new_user['lastName'], 
            new_user['email'],
            new_user['password'],
            new_user['bio'],
            new_user['username'],
            new_user['profileImageUrl'],
            new_user['createdOn'],
            new_user['active'],
            new_user['accountTypeId']
            ))

        id = db_cursor.lastrowid

    data={}
    data["valid"]=True
    data["token"]=id
    
    return json.dumps(data)

def check_user(user):
    with sqlite3.connect("./picnic-fish.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id
        FROM users u
        WHERE u.email = ? AND u.password = ?
        """, (user['email'],
              user['password']
              ))    

        data = db_cursor.fetchone() 

        id = data[0]
        response={}
        response["valid"]=True
        response["token"]=id
    
    return json.dumps(response)
