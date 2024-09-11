class Product():
    def __init__(self,name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        #pass
        return f'{self.name} , {self.weight} , {self.category}'
class Shop:
    _file_name = 'products.txt'
    def get_products(self):
        file = open(Shop._file_name,'r')
        file_name_str = file.read()
        file.close()
        return file_name_str

    def add(self,*product):
        file = open(Shop._file_name, 'a')
        for i in product:
             s =  self.get_products()
             if  i.name in self.get_products()  :
               print(f'Продукт {i.__str__()} уже есть в магазине')
             else:
                 file.write(str(i)+'\n')
        file.close()

s1 = Shop()
p1 = Product('Potato',50.5,'Vegatable')
p2 = Product('Spaghetti',3.4,'Groceries')
p3 = Product('Potato',5.5,'Vegatable')
print(p2)
s1.add(p1,p2,p3)
print(s1.get_products())


