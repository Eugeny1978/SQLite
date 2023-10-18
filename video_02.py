import sqlite3 as sq

# БД открыть соединение в данн случае в том же каталоге. Если такой базы нет то она создастся
#Для БД можно использовать такие расширения: *.db, *.db3, *.sqlite, *.sqlite3

# Не лучший вариант работы с БД, тк при возникновении ошибки программа прервется
# и данные могут быть потеряны.
connent_bd = sq.connect('saper.db')
cursor_bd = connent_bd.cursor() # Объект класса Cursor
# Внутри уже работаем SQL
cursor_bd.execute("""
""")
connent_bd.close() # в конце работы БД необходимо закрыть

# Необходимо использовать Конструктор - коннтекст-менеждер:
with sq.connect('saper.db') as connent_bd:
    cursor_bd = connent_bd.cursor()
    cursor_bd.execute("""
    """)
    # уже не нужен тк как менеджер автоматически закроет базу по окончании работы
    # даже если по ходу кода произошла какая-нибудь ошибка
    # connent_bd.close()

# ЗАДАЧА: Создать Таблицу с Полями:
# name / имя
# sex / пол
# old / возраст игрока
# score / суммарно очков.

# ТИПЫ Данных:
# NULL - значение NULL
# INTEGER - целое число (1-8 байт)
# REAL - вещественное число (8 байт в формате IEEE)
# TEXT - текст (в кодировке БД, обычно utf-8)
# BLOB - двоичные данные, хранятся как есть. используются например для небольших изображений


with sq.connect('saper.db') as connent_bd:
    cursor_bd = connent_bd.cursor()
    cursor_bd.execute("""DROP TABLE  IF EXISTS users""") # удаляет таблицу если существует
    # Создает Таблицу если существует с таким названием
    # Обрати внимание на ограничители NOT NULL, DEFAULT
    # PRIMARY KEY - уникальный ключ позволяет связывать таблицы между собой.
    # Существует встроенный уникальный ключ - rowid
    # Он создается автоматически.
    cursor_bd.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER)""")

