#10: Python SQLite методы fetchall, fetchmany, fetchone, Binary, iterdump
# ЧАСТЬ 2 Binary. Сохранение Бинарных данных на примере Записи и чтения Изображений
import sqlite3 as sq

def readAva(n):
    try:
        with open(f'avas/{n}.jpg', 'rb') as file:
            return file.read()
    except IOError as error:
        print(error)
        return False

def writeAva(name, data):
    try:
        with open(name, 'wb') as file:
            file.write(data)
    except IOError as error:
        print(error)
        return False

    return True


with sq.connect('cars.db') as connect_db:
    connect_db.row_factory = sq.Row # инфа в виде словарей
    cursor_db = connect_db.cursor()
    cursor_db.execute("""
        CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        ava BLOB,
        score INTEGER)
        """)

    cursor_db.execute("SELECT ava FROM users LIMIT 1")
    # img = cursor_db.fetchone()[0] # по индексу по умолчанию если инфа в виде кортежей
    img = cursor_db.fetchone()['ava']

    # img = readAva(1)
    # if img:
    #     binary = sq.Binary(img)
    #     cursor_db.execute("INSERT INTO users VALUES('Nick', ?, 1000)", (binary,))

    writeAva('avas/write_img.jpg', img)
