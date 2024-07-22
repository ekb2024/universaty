# ------- словарь ------
my_dict = {'Andry':25,'Victor':42,'Elena':34}
print('Dict:',my_dict)
print('Existing value:',my_dict['Victor'])
print(my_dict.get('Sergei','Not existing value:'))
my_dict['Svetlana'] = 24
my_dict['Aleksandra'] = 33
# или
my_dict.update({'Ivan':30,'Mila':32})
temp = my_dict.pop('Svetlana')
print(temp)
print(my_dict)

#"------- множество ------"
my_set = {23,45,True,67,12,18,23,12,True}
print(my_set)
my_set.update({100,'stroka'})
#или
my_set.add((23,12,18))
my_set.add(False)
my_set.remove(45)
print(my_set)



