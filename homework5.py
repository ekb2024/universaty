# food = ["apple","cocod","banana"]
# food.append(True)
# food.extend(['string',2])
# food.remove("apple")
# print("1234" in food)
# print(food)
# print(food[0:2:2])
# tuple_1 = 1,2,3,4
# tuple_2 = (1,2,3,4)
# tuple_3 = tuple([1,2,3,4])
# print(tuple_3)
# corteg = (([4,5],"ddd")+(8,9))*3
# print(corteg)
# corteg[0][0] = 2
# print(corteg)


immutable_var = (2,3,3.1456,"i_string",[8,9],True)
print(immutable_var)

#immutable_var[0] = 1
#immutable_var[0] = 1~~~~~~~~~~~~~^^^TypeError: 'tuple' object does not support item assignment
#элементы кортеджа неизменяемые именить можно только элементы внутри обьекта списока
#в кортедже по счету он  4 и меняем первый его элемент

immutable_var[4][0] = 1
print(immutable_var)
mutable_list = [23,45,0.345,"i_string",True]
print(mutable_list)

mutable_list[0] = 11
mutable_list[1] = 22
mutable_list[2] = 3.14
mutable_list[3] = 123456
mutable_list[4] = False
print(mutable_list)

mutable_list[0] = "new_string"
mutable_list[1] = True
mutable_list[2] = 11111
mutable_list[3] = [1,2,3,4,True,"i_new_list"]
mutable_list[4] = False
print(mutable_list)







