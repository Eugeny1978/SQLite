#10: Python SQLite методы
# ЧАСТЬ 4 :memory Создание Временных Баз Данных
import sqlite3 as sq

data = [('car', 'машина'),
        ('house', 'дом'),
        ('tree', 'дерево'),
        ('color', 'цвет'),
        ('dog', 'собака')]

connect_bd = sq.connect(':memory:')
with connect_bd:
    cursor_bd = connect_bd.cursor()
    cursor_bd.execute("""
    CREATE TABLE IF NOT EXISTS eng_rus_dict (
    eng_word TEXT, rus_word TEXT)
    """)
    cursor_bd.executemany("INSERT INTO eng_rus_dict VALUES(?, ?)", data)
    cursor_bd.execute("SELECT * FROM eng_rus_dict WHERE eng_word LIKE 'c%'")
    print(cursor_bd.fetchall())
