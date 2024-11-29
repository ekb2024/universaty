import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute(f' DROP TABLE IF  EXISTS Users')
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                 id INTEGER PRIMARY KEY,
                 username TEXT NOT NULL,
                 email TEXT NOT NULL,
                 age INTEGER,
                 balance INTEGER NOT NULL
                )''')

for i in range(1,11):
  User = f'User{i}'
  example = f' example{i}@gmail.com'
  age = str(i*10)
  cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ? )',
               (User, example, age, 1000))

for i in range(1,11,3):
     cursor.execute(f'DELETE FROM Users WHERE id = {i}')

cursor.execute('SELECT username,email,balance,age FROM Users WHERE age != 60')
table = cursor.fetchall()
for i in table:
    print(f'Имя:{i[0]}|Почта:{i[1]}| Возраст:{i[3]} | Баланс:{i[2]}')

connection.commit()
connection.close()
