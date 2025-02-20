import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()

cursor.execute('SELECT username, age FROM users WHERE age > ?', (25,))
results = cursor.fetchall()

#вывод
for row in results:
    print(row)

connection.close()
