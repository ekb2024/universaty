from threading import Thread
from time import sleep
from random import randint
import queue
class Table:
    def __init__(self,number:int,guest=None):
        self.number = number
        self.guest = guest
class Guest(Thread):
  def __init__(self,name:str):
      self.name_ = name
      super().__init__()
  def run(self):
      sleep(randint(3,10))

class Cafe:
    queue = queue.Queue()
    def __init__(self,*tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        n_table = 0
        for guest_ in guests:
           if n_table < len(tables):
             tables[n_table].guest = guest_.name_
             guest_.start()
             guest_.join()
             print(f'{tables[n_table].guest} сел(-а) за стол номер {tables[n_table].number}')
             n_table +=1
           else:
               Cafe.queue.put(guest_)
               print(f'{guest_.name_}  в очереди".')

    def discuss_guests(self):
        for n_theraed in guests:
           for table in tables:
               if n_theraed.is_alive() == False:
                      if table.guest == n_theraed.name_:
                          print(f'{n_theraed.name_} покушал(-а) и ушёл(ушла)" и "Стол номер {table.number} свободен')
                          table.guest = None
                          if Cafe.queue.empty() == False:
                            guest_ = Cafe.queue.get()
                            table.guest = guest_.name_
                            print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            guest_.start()
                            guest_.join()
        print('\n кафе закрылось :( ')



tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

