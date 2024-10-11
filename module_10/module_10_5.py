import multiprocessing
from datetime import datetime

filenames = [f'./file {number}.txt' for number in range(1, 5)]
def read_info(name):
    all_data=[]
    with open(name,'r') as file:
        for str_ in file:
            all_data.append(str_)

time_old = datetime.now()
for file in filenames:
      read_info(file)
print(f'Линейный вызов: {datetime.now() - time_old}')

if __name__== '__main__':
   time_old = datetime.now()
   with  multiprocessing.Pool(processes=4) as pool:
       pool.map(read_info,filenames)
   print(f'Многопроцессный : {datetime.now() - time_old}')




