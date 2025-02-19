import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()
#Созд табл
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
#сохр
connection.commit()
connection.close()
