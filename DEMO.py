import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()
#Созд индекса emal
cursor.execute('CREATE INDEX idx_email ON Users (email)')
#сохр
connection.commit()
connection.close()
