import sqlite3 as sq

with sq.connect("saper.db") as connect_db:
    cursor = connect_db.cursor()

    cursor.execute("""
    SELECT * FROM users 
    WHERE score >= 20000
    ORDER BY score DESC
    LIMIT 3
    """)
    # selection1 = cursor.fetchall() # вариант сразу извлечь все
    # print(selection1)

    # selection3 = cursor.fetchone() # cursor.fetchone() - возвращает первую запись
    # print(selection3)
    # selection4 = cursor.fetchmany(2) # cursor.fetchmany(size=5) - возращает число записей но не более
    # print(selection4)
    #
    for selection2 in cursor: # вариант обойти циклом. Экономит Память выгрузка происходит частями
        print(selection2)
    # Обрати внимание после извлечения записи "пропадают. чтобы снова вывести выборку - необходимо снова послать запрос в БД
