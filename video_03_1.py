# ПРИМЕРЫ: СМ ФАЙЛ с базой Данных, вкладка SQL

# INSERT - добавление в таблицу
# SELECT - выбора данных из таблиц

# # Запись в поля
# INSERT INTO <table_name> (<column_name1>, <column_name2>, ...) VALUES (<value1>, <value1>, ...)
#
# # Запись в поля по порядку
# INSERT INTO <table_name> VALUES (<value1>, <value1>, ...)

# Выбор Полей из таблицы
# SELECT (<column_name1>, <column_name2>, ...) FROM <table_name>

# Выбор Полей из таблицы по условию
# SELECT (<column_name1>, <column_name2>, ...) FROM <table_name> WHERE <условие>
# == или =, <, >, >=, <=, !=, BETWEEN

# AND - условнное И
# OR - условное ИЛИ
# NOT - Условное НЕ
# IN - вхождение в Множество значений
# NOT IN - Не вхождение в Множество значений
# Приоритет операции AND выше чем ORю Если необходимо изменнить приоритет - скобки.
# Приоритет: NOT -> AND -> OR
# ORDER BY <column_name> - Сортировка / ASC - по возрастанию (можно не прописывать) / DESC - по убыванию
# LIMIT - макс кол-во записей в выборке LIMIT <max> [OFFSET offset] либо LIMIT <offset, max>

# -- INSERT INTO users VALUES (55, "Jane", 2, 11, 33877)
# -- INSERT INTO users (name, old, score) VALUES ("Karas", 14, 72898)
#
# -- SELECT name, score FROM users
# -- SELECT * FROM users
# -- SELECT * FROM users WHERE sex==2
# -- SELECT * FROM users WHERE score >= 50000
# -- SELECT * FROM users WHERE score>=50000 AND sex=1
# -- SELECT * FROM users WHERE score BETWEEN 20000 AND 40000
# -- SELECT * FROM users WHERE score > 20000 AND sex == 2
# -- SELECT * FROM users WHERE score > 30000 OR old > 14
# -- SELECT * FROM users WHERE old IN (12, 15, 17)
# SELECT * FROM users WHERE score > 15000
# ORDER BY score DESC
# -- LIMIT 1, 3
# LIMIT 3 OFFSET 1