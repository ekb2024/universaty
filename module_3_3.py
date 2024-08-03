def print_params(a = 1, b = "строка",c = True):
    print(a,b,c)

# 1.Функция с параметрами по умолчанию:
print_params(a =22)
print_params(b =444,c = 123)
print_params(c = [1, 2, 3])

# 2.Распаковка параметров:
vales_list = [101.23,"я просто строка",False]
vales_dict = {'a':890.01,"b":False,"c":'строчка'}
print_params(*vales_list )
print_params(**vales_dict )

# 3.Распаковка + отдельные параметры:
values_list_2 = [111.001,'и опять строка']
print_params(*values_list_2, 42)





