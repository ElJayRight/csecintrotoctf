import sqlite3

def build():
    connection = sqlite3.connect('dbf.db')
    cursor = connection.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS data (
        username TEXT PRIMARY KEY,
        password TEXT,
        uni TEXT
    )
'''
    cursor.execute(create_table_query)
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS flags (
        id INT PRIMARY KEY,
        value TEXT
    )
'''
    cursor.execute(create_table_query)
def check_user(username):
    connection = sqlite3.connect('dbf.db')
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

def add_account(username,password,uni):
    connection = sqlite3.connect('dbf.db')
    cursor = connection.cursor()

    insert_query = '''
    INSERT INTO data (username,password,uni)
    VALUES (?, ?, ?)
'''
    user_data = (username, password,uni)
    cursor.execute(insert_query, user_data)
    connection.commit()
    connection.close()

def add_flag(id,flag):
    connection = sqlite3.connect('dbf.db')
    cursor = connection.cursor()

    insert_query = '''
    INSERT INTO flags (id, value)
    VALUES (?, ?)
'''
    user_data = (id, flag)
    cursor.execute(insert_query, user_data)
    connection.commit()
    connection.close()

def login_check(username):
    connection = sqlite3.connect('dbf.db')
    cursor = connection.cursor()

    check_query = "SELECT username,uni FROM data WHERE username = '%s'" % username
    try:
        cursor.execute(check_query)
        result = cursor.fetchone()

        connection.close()
        return result
    except sqlite3.OperationalError as e:
        return e


if __name__ == "__main__":
    build()
    add_flag('1','     Get ready for a few fake flags!')
    add_flag('2','     How many fake flags are there?')
    add_flag('3','Is there a better way to do this?')
    add_flag('4','CSEC{SqL_un10n_1nj3ct10n5_fTw}')
    add_account('eljay','youwontguessthis','usyd')