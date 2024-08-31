class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name
    def eat(self, food):
            if food.edible == False:
                self.alive = False
                print(f'{self.name} не стал есть {food.name}')
            else:
                self.fed = True
                print(f'{self.name} съел {food.name}')
class Plant:
    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name
class Mammal(Animal):
      pass
class Predator(Animal):
      pass
class Flower(Plant):
      pass
class Fruit(Plant):
    def __init__(self, name, edible=True):
        self.edible = True
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Завондной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


