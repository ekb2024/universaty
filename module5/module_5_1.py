class Hause:
    def __init__(self,name,number_of_floors):
        self.name =  name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
                print('Такого этажа не существует')
                return
        for i in range(1,new_floor+1):
               print(i)
        ### или так
        # i = 0
        # while i < new_floor:
        #        i += 1
        #        print(i)




h1 = Hause('ЖК Горский',18)
h2 = Hause('Домик в деревне',2)
h1.go_to(5)
h2.go_to(10)
