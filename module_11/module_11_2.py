import inspect
class  exempels_obj:
    proct = [1,23,4]
    y = 12
    def __init__(self):
        pass
    def fun_exempel(self,h:int,x:int,number:int):
        for i in number:
            h = i * x+exempels_obj.y
        return h

def  introspection_info(obj):
     info_obj = {}
     info_attr = {}
     info_metod = {}
     info_obj.update({'type':type(obj)})
     info_obj.update({'attributes': dir(obj)})
     info_obj.update({'module': inspect.getmodule(obj)})
     for i in dir(obj):
         info_attr.update({i: getattr(obj,i)})
         if inspect.ismethod(getattr(obj,i)) == True:
             info_metod.update({i:getattr(obj,i)})
     return  f'атрибуты обьекта\n {info_obj}' ,f'своиства атрибутов\n{info_attr}' ,f'методы и атрибуты \n{info_metod}'

obj = exempels_obj()
print(introspection_info(obj)[0])
print(introspection_info(obj)[1])
print(introspection_info(obj)[2])

print(introspection_info(42)[0])
print(introspection_info(42)[1])


