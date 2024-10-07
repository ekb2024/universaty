from threading import Thread,Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        super().__init__()
    def deposit(self):
           random_ = 0
           for i in range(100):
                random_ = randint(50, 500)
                self.balance += random_
                print(f'Пополнение: {random_}. Баланс: {self.balance}')
                sleep(0.001)
                if self.balance >= 500 and self.lock.locked() == True:
                  self.lock.release()
    def take(self):
        for i in range(100):
            random_ = randint(50, 500)
            print(f'Запрос на {random_}')
            if random_ <= self.balance:
                self.balance -= random_
                sleep(0.001)
                print(f'Снятие:{random_}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
