#10: Python SQLite методы fetchall, fetchmany, fetchone, Binary, iterdump
# ЧАСТЬ 1 fetchall, fetchmany, fetchone. Извлечение инфы по запросам
import sqlite3 as sq

with sq.connect('cars.db') as connect_db:
    connect_db.row_factory = sq.Row # Если хотим строки записей в виде dict {}. По умолчанию - кортежи turple ()
    cursor_db = connect_db.cursor()

    # cursor_db.execute("SELECT model, price FROM cars")
    # rows = cursor_db.fetchall()
    # print(rows, '\n')
    #
    # cursor_db.execute("SELECT model, price FROM cars")
    # rows = cursor_db.fetchone()
    # print(rows, '\n')
    #
    # cursor_db.execute("SELECT model, price FROM cars")
    # rows = cursor_db.fetchmany(3)
    # print(rows, '\n')

    cursor_db.execute("SELECT model, price FROM cars")
    for select in cursor_db:
        # print(select)
        print(select['model'], '|', select['price'])