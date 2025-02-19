import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

#вывод
for user in users:
    print(user)

#сохр
connection.commit()
connection.close()
