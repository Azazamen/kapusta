import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')

connection.close()
