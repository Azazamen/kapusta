import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()

# Изменение данных
cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

#сохр
connection.commit()
connection.close()
