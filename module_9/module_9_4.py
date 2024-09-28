from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y:x==y, first,second)))

def get_advanced_wtiter(file_name):
    def write_everything(*data_set):
        for one in data_set:
           with open(file_name,'a',encoding='utf-8') as file:
              file.write(f'{one}\n')
    return write_everything

class MysticBall:
    def __init__(self,*words):
        self.words = words
    def __call__(self,*words):
       return choice(self.words)



write = get_advanced_wtiter('examlple.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())

