#5: Python SQLite  агрегирование и группировка GROUP BY

# Агрегирующие Функции (выполняются всегда в последнюю очередь)
# count()
# sum()
# avr()
# min()
# max()
# SELECT user_id FROM games WHERE user_id == 1
# SELECT count(user_id) FROM games WHERE user_id == 1
# SELECT count() FROM games WHERE user_id == 1
# SELECT count() as count_games FROM games WHERE user_id == 1
# SELECT sum(score) as scores FROM games WHERE user_id == 1


# ГРУППИРОВКА Записей
# SELECT sum(score) as scores FROM games GROUP BY (user_id)
# SELECT user_id, sum(score) as scores FROM games GROUP BY (user_id)
#
# SELECT user_id, sum(score) as sum_scores
# FROM games
# WHERE score > 250
# GROUP BY user_id
# ORDER BY sum_scores DESC
# LIMIT 3