import sqlite3


def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute(f' DROP TABLE IF  EXISTS Products')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                     id INTEGER PRIMARY KEY,
                     title TEXT NOT NULL,
                     description TEXT NOT NULL,
                     price INTEGER NOT NULL
                    )''')
    description = ['150 u венфетомина', '1000 мг рыбьего жира', 'втамин с L -аскорбиновая кислота','50 активных ингредиентов']
    list_vit = ['benfotiamine', 'omega3', 'sambucol', 'ultra men']
    for i  in range(4):
       cursor.execute('INSERT INTO Products (title,description,price) VALUES (?, ?, ? )',
                   (list_vit[i], description[i],(i+10)**2))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_records = cursor.fetchall()
    vit =[]
    for i in all_records:
       vit.append({'Название':i[1],'Описание':i[2],'Цена':i[3]})
    return vit
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    #cursor.execute(f' DROP TABLE IF  EXISTS Users')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                     id INTEGER PRIMARY KEY,
                     username TEXT NOT NULL,
                     email TEXT NOT NULL,
                     age INTEGER,
                     balance INTEGER NOT NULL
                    )''')
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ? )',
                   (username, email, age, 1000))

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('not_telegram.db')
    cursor= connection.cursor()
   # cursor.execute(f'SELECT username FROM Users WHERE username = {username}')
    cursor.execute(f'SELECT username FROM Users WHERE username = "{username}"')
    if len(cursor.fetchall())==0: is_ = False
    else: is_ =True
    connection.close()
    return is_

if __name__=='__main__':
    #initiate_db()
    #print(get_all_products())
    print(is_included('User'))