#8: Python SQLite вложенные SQL-запросы
#
# -- SELECT mark FROM marks
# -- WHERE id=2 AND subject LIKE 'Си'
# -- SELECT name, subject, mark FROM marks
# -- JOIN students ON students.ROWID = marks.id
# -- WHERE mark > 3 AND subject LIKE 'Си'
#
# -- SELECT name, subject, mark FROM marks
# -- JOIN students ON students.ROWID = marks.id
# -- WHERE
# -- 	mark > (SELECT mark FROM marks WHERE id=2 AND subject LIKE 'Си')
# -- ND subject LIKE 'Си'
#
# -- SELECT avg(mark) FROM marks WHERE id=2
#
# -- SELECT name, subject, mark FROM marks
# -- JOIN students ON students.ROWID = marks.id
# -- WHERE
# -- 	mark > (SELECT avg(mark) FROM marks WHERE id=2)
# -- 	AND subject LIKE 'Си'
#
# -- SELECT * FROM students WHERE sex=2
#
# -- INSERT INTO female
# -- SELECT NULL, name, sex,old FROM students WHERE sex=2
#
# -- UPDATE marks SET mark = 0
# -- WHERE mark <= (SELECT min(mark) FROM marks WHERE id=1)
#
# DELETE FROM students
# WHERE old < (SELECT old FROM students WHERE id=3)