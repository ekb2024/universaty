class  IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message
class  IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message
class Car:
    def __init__(self,model,_vin,_numbers):
        self.model = model
        self._vin = _vin
        self._numbers = _numbers
        self._is_valid_vin(_vin)
        self._is_valid_number(_numbers)
    def _is_valid_vin(self, vin_number):
          if not isinstance(vin_number,int):
             raise IncorrectVinNumber('Некорректный тип vin номер')
          if vin_number < 100000 or vin_number > 9999999:
             raise IncorrectVinNumber('Неверный диапазон для vin номера')
          return True
    def _is_valid_number(self,numbers):
        if not isinstance(numbers,str):
           raise  IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
           raise  IncorrectCarNumbers('Неверная длина номера')


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')