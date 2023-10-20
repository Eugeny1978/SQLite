#9: Python SQLite методы execute, executemany, executescript, commit, rollback и свойство lastrowid
import sqlite3 as sq

# cars = [
#     ('Audi', 52642),
#     ('Mersedes', 57125),
#     ('Skoda', 9500),
#     ('Volvo', 32000),
#     ('Bentley', 350500)
# ]
#
#
# with sq.connect('cars.db') as connent_bd:
#     cursor_bd = connent_bd.cursor()
#     cursor_bd.execute("""
#     CREATE TABLE IF NOT EXISTS cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER)
#     """)

    # 1й Способ
    # cursor_bd.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    # cursor_bd.execute("INSERT INTO cars VALUES(2, 'Mersedes', 57125)")
    # cursor_bd.execute("INSERT INTO cars VALUES(3, 'Skoda', 9500)")
    # cursor_bd.execute("INSERT INTO cars VALUES(4, 'Volvo', 32000)")
    # cursor_bd.execute("INSERT INTO cars VALUES(5, 'Bentley', 350500)")

    # 2й Способ (Неименованные Параметры)
    # for car in cars:
    #     cursor_bd.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # 3й Способ (Неименованные Параметры)
    # cursor_bd.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # 4й Способ (Именованные Параметры)
    # cursor_bd.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 50000})
    # cursor_bd.execute("""UPDATE cars SET price = :Price
    #                 WHERE model LIKE 'B%'""", {'Price': 370000})
    # cursor_bd.execute("""UPDATE cars SET price = :Price
    #                     WHERE model LIKE :Model """, {'Price': 40000, 'Model': 'Volvo'})

    # 5й Способ (скрипт. только запросы без параметров!)
    # cursor_bd.executescript("""UPDATE cars SET price = price-1500 WHERE model LIKE 'V%' ;
    #                         INSERT INTO cars VALUES(NULL, 'BMW', 27800)""" )

    # Автоматически выполняются
    # connent_bd.commit()
    # connent_bd.close()

# connect_bd = None
# try:
#     connect_bd = sq.connect('cars.db')
#     cursor_bd = connect_bd.cursor()
#
#     cursor_bd.execute("""CREATE TABLE IF NOT EXIST cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER)
#     """)
#
#     cursor_bd.executescript("""
#     DELETE FROM cars WHERE model LIKE 'A%';
#     UPDATE cars SET price = price+1200""")
#
#     connect_bd.commit() # сохранение внесенных изменений
#
# except sq.Error as error:
#     if connect_bd: connect_bd.rollback()  # откатывает базу и все внесенные изменения убираются
#     print('Ошибка Выполнения запроса')
# finally:
#     if connect_bd: connect_bd.close() # закрытие БД

# connect_bd = None
# try:
#     connect_bd = sq.connect('cars.db')
#     cursor_bd = connect_bd.cursor()
#
#     cursor_bd.executescript("""
#     CREATE TABLE IF NOT EXISTS cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER);
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Audi', 52642);
#     INSERT INTO cars VALUES(NULL, 'Mersedes', 57125);
#     INSERT INTO cars VALUES(NULL, 'Skoda', 9500);
#     INSERT INTO cars VALUES(NULL, 'Volvo', 32000);
#     INSERT INTO cars VALUES(NULL, 'Bentley', 350500);
#     UPDATE cars SET price = price+1200
#     """)
#
#     connect_bd.commit() # сохранение внесенных изменений
#
# except sq.Error as error:
#     if connect_bd: connect_bd.rollback()  # откатывает базу и все внесенные изменения убираются (после метки BEGIN)
#     print('Ошибка Выполнения запроса')
# finally:
#     if connect_bd: connect_bd.close() # закрытие БД

with sq.connect('cars.db') as connect_db:
    cursor_db = connect_db.cursor()
    cursor_db.executescript("""
    CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER);
    CREATE TABLE IF NOT EXISTS cust (
    name TEXT,
    trade_in INTEGER,
    buy INTEGER);
    """)
    cursor_db.execute("INSERT INTO cars VALUES(NULL, 'Lada', 1500)")
    last_row_id = cursor_db.lastrowid
    buy_car_id = 2
    cursor_db.execute("INSERT INTO cust VALUES('Fedor', ?, ?)", (last_row_id, buy_car_id))
