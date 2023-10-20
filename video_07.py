#7: Python SQLite оператор UNION объединения нескольких таблиц

# -- SELECT * fROM tab1
# -- UNION
# -- SELECT * FROM tab2
#
# -- SELECT score as score_value, `from` FROM tab1
# -- UNION
# -- SELECT value, `from` FROM tab2
#
# -- SELECT score FROM tab1
# -- UNION
# -- SELECT value FROM tab2
#
# -- UPDATE tab1 SET `from` = 'tab2'
# -- UPDATE tab1 SET `from` = 'tab1'
#
# -- SELECT score, 'val from table 1' as adress FROM tab1
# -- UNION
# -- SELECT value, 'val from table 2' FROM tab2
#
# -- SELECT score, 'val from table 1' as adress FROM tab1
# -- UNION
# -- SELECT value, 'val from table 2' FROM tab2
# -- ORDER BY adress
#
# SELECT score, 'val from table 1' as adress FROM tab1
# UNION
# SELECT value, 'val from table 2' FROM tab2
# ORDER BY score DESC

# UNION - оставляет только уникальные записи!
