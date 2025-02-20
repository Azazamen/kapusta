import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()

##cursor.execute('SELECT age, AVG(age) FROM users GROUP BY age')
##results = cursor.fetchall()
###вывод
##for row in results:
##    print(row)
##
###фильтр по ср возраст >30
##cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
##filtered_results = cursor.fetchall()
##for row in filtered_results:
##    print(row)

cursor.execute('SELECT age, AVG(age) FROM users ORDER BY age DESC')
results = cursor.fetchall()
#вывод
for row in results:
    print(row)

connection.close()
