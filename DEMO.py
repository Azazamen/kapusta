import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()

#добавление нового польз
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

#сохр
connection.commit()
connection.close()
