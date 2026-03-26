#day 002 - OOP
class Shape:
    
    def __init__(self,shape):
        self.shape = shape
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        print(f"Area of Circle:{3.14 * self.radius * self.radius}") 
    
class Rectangle(Shape):
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length
    
    def area(self):
        print(f"Area of Rectangle:{self.breadth * self.length}") 

shapes = [Circle(5),Rectangle(4,6)]

for shape in shapes:
    shape.area()