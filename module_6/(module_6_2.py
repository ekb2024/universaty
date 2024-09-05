class Vehicle:
    _COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'whlle']
    def __init__(self,owner,_model,_color,_engine):
       self.owner = owner
       self._model = _model
       self._color = _color
       self._engine = _engine

    def get_model(self):
        return f'Модель :{self._model}'
    def get_horsepower(self):
        return f'Мощность двигателя {self._engine}'
    def get_color(self):
        return f'Цвет:{self._color}'
    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self._color = "\033[32m{}".format(new_color.upper())

        else:
         print("\033[31m{}".format(f'Нельзя сменить цвет на {new_color}'),"\033[0m")

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец:{self.owner}',"\033[0m")

class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos','Toyota Mark||','blue','500')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BlAck')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()



