import sqlite3

#Создаём подключение к бд (создастся)
connection = sqlite3.connect ('my_db.db')
cursor = connection.cursor()

##cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser2', 'newuser2@example.com', 30))
##connection.commit()
##cursor.execute('SELECT age, AVG(age) FROM users GROUP BY age')
##results = cursor.fetchall()
###вывод
##for row in results:
##    print(row)

###фильтр по ср возраст >30
##cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
##filtered_results = cursor.fetchall()
##for row in filtered_results:
##    print(row)
##
##cursor.execute('SELECT age, AVG(age) FROM users ORDER BY age DESC')
##results = cursor.fetchall()
###вывод
##for row in results:
##    print(row)

##cursor.execute('''
##SELECT username, age, AVG(age)
##FROM Users
##GROUP BY age
##HAVING AVG(age) > ?
##ORDER BY age DESC
##''', (28,))
##results = cursor.fetchall()
##for row in results:
##    print(row)

##cursor.execute('SELECT COUNT(*) FROM Users')
##total_users = cursor.fetchone() [0]
##print('Общее количество пользователей:', total_users)
##cursor.execute('SELECT SUM(age) FROM Users') 
##total_age = cursor.fetchone() [0]
##print('Общее сумма возрастов пользователей:', total_age)
##cursor.execute('SELECT AVG(age) FROM Users') 
##average_age = cursor.fetchone() [0]
##print('Средний возраст пользователей:', average_age)
##cursor.execute('SELECT MIN(age) FROM Users') 
##min_age = cursor.fetchone() [0]
##print('Минимальный возраст пользователей:', min_age)
##cursor.execute('SELECT MAX(age) FROM Users') 
##max_age = cursor.fetchone() [0]
##print('Минимальный возраст пользователей:', max_age)

##cursor.execute('''
##SELECT username, age
##FROM Users
##WHERE age = (SELECT MAX(age) FROM Users)
##''')
##old_users = cursor.fetchall()
##for row in old_users:
##    print(row)

cursor.execute('SELECT * FROM Users ')
results = cursor.fetchall()
#вывод
for row in results:
    print(row)

connection.close()
