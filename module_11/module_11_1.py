import random
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



## ---------------------------- numpy ------------------------------------
def gen_line(n_random: int, x_len: int):
  y = np.array([np.sin(i) for i in range(0, x_len)])
  x = np.array([np.cos(i) for i in range(0, x_len)])
  x_ = np.array([i for i in range(0, x_len)])
  y_ = np.array([i + random.randint(0, n_random) for i in range(0, x_len)])
  # полиномиальная функция из numpy
  f_ = np.poly1d(np.polyfit(x_, y_, 4))
  return x, y, x_, y_, f_

##--------------------------------------- requests  pandas -----------------------------
def my_time():
    my_ip = requests.get('https://ipv4-internet.yandex.net/api/v0/ip')
    # найдем свой ip если найдется
    if my_ip.status_code == 200:
         region_time = requests.get(f"http://ip-api.com/json/{my_ip.json()}?lang=ru")
         # найдем регион город и прова
         if region_time.status_code == 200:
           # проще словарь но покажем и запихнем в  pandas раз таk
           region_ = pd.Series(region_time.json(),index=['country','regionName','city','timezone','org', 'query'])
           # вызовем местное время
           time = requests.get(f'https://tools.aimylogic.com/api/now?tz={region_['timezone']}')
           if time.status_code == 200:
             region_time_ip = pd.Series(time.json(),index=['formatted','weekDay'])
             return f' и так по {region_['query']} {region_['country']} {region_['regionName']} {region_['city']} {region_['org']} время {region_time_ip['formatted']} день {region_time_ip['weekDay']}'
           else:
             return 'не нашел время'
         else:
           return 'не нашел место'
    else:
      return 'не нашел ip'


def get_data(symbol:str,interval:str,limit:int):
    url = f'https://api.binance.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}'
    result_get = requests.get(url).json()
    data = pd.DataFrame(result_get)
    data.to_csv(f'{symbol}.csv')
    data = pd.read_csv(f'{symbol}.csv')
    return data

## по IP время регион город и .тд
print(my_time())
## запрашиваем данные с биржи пишем в с помощью в файл pandas ..читаем
print(get_data('BTCUSDT','1h',1000))
## генерим линиии и пиксели по random в массивы проводим развесовку(полиномиальная) рисуем
x, y, x_, y_, f_ = gen_line(100, 100)


## ------------------------- matplotlib -----------------------------
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12, 8))
axes[0].plot(x, y)
axes[1].scatter(x_,y_)
axes[1].scatter(x_, f_(x_))
plt.show()


