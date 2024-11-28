import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="Users"')
result = cursor.fetchone()

if result is not None:
        print("если таблица Users существует... удалим ")
        cursor.execute(f'DROP TABLE Users')

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


cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != ?', (500, 0))
cursor.execute('DELETE FROM Users WHERE id in (?,?,?,?)', (1,4,7,10))
cursor.execute('DELETE FROM Users WHERE id = 6')
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users ')

all_balance = cursor.fetchone()[0]
print(all_balance/total_users)

connection.commit()
connection.close()