import sqlite3

def build():
    connection = sqlite3.connect('api_3.db')
    cursor = connection.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS data (
        username TEXT PRIMARY KEY,
        password TEXT
    )
'''
    cursor.execute(create_table_query)

    connection.commit()
    connection.close()

def check_user(username):
    connection = sqlite3.connect('api_3.db')
    cursor = connection.cursor()

    check_query = '''
    SELECT username FROM data WHERE username = ?
'''
    cursor.execute(check_query, (username,))
    result = cursor.fetchone()

    connection.close()
    if result:
        return True
    return False

def add_account(username,password):
    connection = sqlite3.connect('api_3.db')
    cursor = connection.cursor()

    insert_query = '''
    INSERT INTO data (username,password)
    VALUES (?, ?)
'''
    user_data = (username, password)
    cursor.execute(insert_query, user_data)
    connection.commit()
    connection.close()

def login_check(username,password):
    connection = sqlite3.connect('api_3.db')
    cursor = connection.cursor()

    check_query = '''
    SELECT username FROM data WHERE username = ? AND password = ?
'''
    cursor.execute(check_query, (username,password))
    result = cursor.fetchone()

    connection.close()
    if result:
        return True
    return False


if __name__ == "__main__":
    build()