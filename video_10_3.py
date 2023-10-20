#10: Python SQLite методы fetchall, fetchmany, fetchone, Binary, iterdump
# ЧАСТЬ 3 iterdump Воссоздание Таблицы
import sqlite3 as sq


with sq.connect('cars.db') as connect_db:
    cursor_db = connect_db.cursor()

    # Записи в Базу
    # for sql in connect_db.iterdump():
    #     print(sql)

    # # Запишу эти записи в файл
    # with open('sql_dump.sql', 'w') as file:
    #     for sql in connect_db.iterdump():
    #         file.write(sql)

    # Предварительно удалю базу "cars" в программе DB Browser SAQLite
    # Теперь восстановлю базу из нашего файла
    with open('sql_dump.sql', 'r') as file:
            sql = file.read()
            cursor_db.executescript(sql)


