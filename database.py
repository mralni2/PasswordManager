import os.path
import sqlite3

from aes import start_decrypt_file, main_key

if os.path.exists('etc.db'):
    start_decrypt_file('etc.db', main_key)
db = sqlite3.connect('etc.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, profile_password TEXT)''')


# Создать таблицу с логином пользователя
def create_login_table(login):
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS''' + ''' ''' + "'" + login + "'" +
        '''(id INTEGER PRIMARY KEY, service TEXT, login TEXT, email TEXT, password TEXT)''')


# Добавить в таблицу логина пользователя данные
def insert_data_to_login_table(login, data):
    cursor.execute(
        '''INSERT INTO''' + ''' ''' + "'" + login + "'" '''(service, login, email, password) VALUES (?, ?, ?, ?)''',
        (data[0], data[1], data[2], data[3]))
    db.commit()


# Выбрать все данные из таблицы логина пользователя
def selection_all_data_from_login_table(login):
    cursor.execute('''SELECT * FROM''' + ''' ''' + "'" + login + "'" + '''ORDER BY service''')
    return cursor.fetchall()


# Выбрать данные одной строки (key) в таблице логина пользователя
def selection_one_data_from_login_table(login, key):
    cursor.execute('''SELECT * FROM''' + ''' ''' + "'" + login + "'" + ''' ''' + '''WHERE id=?''', (key,))
    return cursor.fetchall()


# Удалить данные одной строки (key) в таблице логина пользователя
def delete_one_data_from_login_table(login, key):
    cursor.execute('''VACUUM''')
    cursor.execute('''DELETE FROM''' + ''' ''' + "'" + login + "'" + ''' ''' + '''WHERE id=?''', (key,))
    db.commit()


# Обновить данные в строке (key) в таблице логина пользователя
def update_data_in_login_table(login, data, key):
    cursor.execute(
        '''UPDATE''' + ''' ''' + "'" + login + "'" + ''' ''' + '''SET service=?, login=?, email=?, password=? WHERE 
        id=?''', (data[0], data[1], data[2], data[3], key,))
    db.commit()


# Обновить все пароли в таблице логина пользователя
def update_passwords_in_login_table(login, data, key):
    cursor.execute(
        '''UPDATE''' + ''' ''' + "'" + login + "'" + ''' ''' + '''SET password=? WHERE 
        id=?''', (data, key,))
    db.commit()


# Поиск по сервису в таблице логина пользователя
def search_service_in_login_table(login, service):
    service = ('%' + service + '%',)
    cursor.execute('''SELECT * FROM''' + ''' ''' + "'" + login + "'" + ''' ''' + ''' WHERE service LIKE ?''', service)
    return cursor.fetchall()


# Находит одинаковые пароли в таблице логина пользлвателя
def selection_password_in_login_table(login):
    cursor.execute(
        '''SELECT *
        FROM''' + ''' ''' + "'" + login + "'" + ''' ''' +
        '''WHERE password IN
        (SELECT password FROM''' + ''' ''' + "'" + login + "'" + ''' ''' +
        '''GROUP BY password  HAVING COUNT(*)>1)''')
    return cursor.fetchall()


# Добавить пользователя в таблицу профилей (регистрация)
def insert_user_to_users_table(user_info):
    if find_user(user_info[0]) is None:
        cursor.execute('''INSERT INTO users (username, profile_password) VALUES (?, ?)''', user_info)
        db.commit()
        return 0
    else:
        return None


# Поиск уже существующего профиля / 70 database
def find_user(user_info):
    cursor.execute('''SELECT * FROM users WHERE username = ?''', ([user_info]))
    find = cursor.fetchone()
    if find is not None:
        return find
    else:
        return None


# Авторизация
def login_user(user_info):
    find = find_user(user_info[0])
    if find is not None:
        if find[1] == user_info[1]:
            return 0
    else:
        return None
