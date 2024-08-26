class House:
    houses_history = []
    __new_self = None
    def __new__(cls, *args, **kwargs):
        cls.houses_history += args
        __new_self = super().__new__(cls)
        return __new_self
    def __init__(self,name,number_of_floors):
        self.name =  name
        self.number_of_floors = number_of_floors
    def __del__(__new_self):
          print(f'{__new_self.name},снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
