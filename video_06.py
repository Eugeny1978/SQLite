#6: Python SQLite оператор JOIN для формирования сводного отчета

# JOIN <table_name> ON <условия связывания>

# SELECT name, sex, games.score FROM games
# JOIN users ON games.user_id = users.rowid

# -- SELECT name, sex, games.score FROM games
# -- -- JOIN users ON games.user_id = users.rowid
# -- -- INNER JOIN users ON games.user_id = users.rowid
# -- LEFT JOIN users ON games.user_id = users.rowid
#
# SELECT games.user_id, users.name, users.sex, sum(games.score) as sum_scores FROM games
# LEFT JOIN users ON games.user_id == users.rowid
# GROUP BY games.user_id
# ORDER BY sum_scores DESC

