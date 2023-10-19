# UPDATE - измененние данных в записях
# DELETE  - удаление записей из таблицы
#
# UPDATE table_name SET <column>=<new value> WHERE <condition>

# Применение оператора LIKE:
# % - любое продолжение строки
# _ - любой символ

# UPDATE users SET score = 55555 WHERE sex=2
# UPDATE users SET score = 55555
# UPDATE users SET score = score+3500 WHERE sex=2
# UPDATE users SET score = score + 77000 WHERE ROWID=5
# UPDATE users SET score = score + 2500 WHERE name LIKE 'Bob'
# UPDATE users SET score = score + 2500 WHERE name LIKE 'Bo_'
# UPDATE users SET score = score + 2500 WHERE name LIKE 'B%'
# UPDATE users SET old = 13, score = 10000  WHERE sex=2
#
# DELETE FROM users WHERE ROWID IN (7, 10)