import  math
class Figure:
    sides_count = 0
    def __init__(self,_color,_sides):
        self._color = []
        self._sides = []
        self.filled = True

    def get_color(self):
        return self._color
    def _is_valid_color(self,r,g,b):
        if self.valid_color(r) == True and self.valid_color(g) == True and self.valid_color(b) == True:
            return True
        else:
            return False
    def valid_color(self,rgb):
        if isinstance(rgb, int) and rgb >= 0 and rgb <= 255:
            return True
        else:
            return  False
    def set_color(self,r,g,b):
         if self._is_valid_color(r, g, b) == True:
              self._color =list(self._color)
              self._color[0] = r
              self._color[1] = g
              self._color[2] = b

    def _is_valid_sides(self, *args):
        for i in args:
            if i < 0:
              return False
        if len(Figure.sides_count) != len(args):
              return  False
        return True

    def get_sides(self):
        return self._sides

    def set_sides(self,*new_sides):
       if  self.sides_count == len(new_sides):
            self._sides = list(new_sides)

    def __len__(self):
        perimetr = 0
        for i in self._sides:
             perimetr += i
        return perimetr

class Cicle(Figure):
     sides_count = 1
     def __init__(self, _color, *_sides):
         self._color = list(_color)
         if len(_sides) != Cicle.sides_count:
             self._sides = [1]
         else:
             self._sides = _sides
             _radius = _sides[0] / (2 * math.pi)

     def get_square(self,):
         return  self._sides[0] ** 2 / 4 * math.pi

class Triangle(Figure):
    sides_count = 3
    def __init__(self,_color,*_sides):
      self._color = _color
      self._sides = []
      if len(_sides) == Triangle.sides_count:
          for i in range(Triangle.sides_count):
              self._sides.append(*_sides)
      if len(_sides) != Triangle.sides_count and len(_sides) > 1:
          for i in range(Triangle.sides_count):
              self._sides.append(1)
    def get_square(self):
        if Triangle.sides_count == 3:
            p = (self._sides[0] + self._sides[1] + self._sides[2])*0.5
            return  p*(p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2])
class Cube(Figure):
    sides_count = 12
    def __init__(self,_color,*_sides):
      self._color = _color
      self._sides = []
      if len(_sides) == 1:
          for i in range(Cube.sides_count):
              self._sides.append(*_sides)
      if len(_sides) != Cube.sides_count and len(_sides) > 1:
          for i in range(Cube.sides_count):
              self._sides.append(1)
    def get_volume(self):
            return self._sides[0] ** 3


circle1= Cicle((200,200,100),10)
cube1 = Cube((222,35,130),6)
circle1.set_color(55,66,77)
print(circle1.get_color())
cube1.set_color(300,70,15)
print(cube1.get_color())
cube1.set_sides(5,3,12,4,5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
