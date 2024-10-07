from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, power):
        self.name_ = name
        self.power_ = power
        super().__init__()
    def run(self):
        print(self.name_,'на нас напали!')
        n_day = 0
        n_life = 100
        while n_life >= self.power_:
           n_life -= self.power_
           n_day += 1
           sleep(1)
           print(f'{self.name_} сражается {n_day} дней ..., осталось {n_life} воинов')

        print(f'{self.name_} одержал победу спустя {n_day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
