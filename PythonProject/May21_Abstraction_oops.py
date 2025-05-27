from abc import ABC, abstractmethod

class Shape(ABC):   # shape is abstraction class
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def parameter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,lenght):
        self.width = width
        self.lenght = lenght

    def area(self):    #instance method
        return self.lenght * self.width

    def parameter(self):
        return self.lenght + self.width

x = Rectangle(5,2)
print(x.area())
print(x.parameter())

# abstraction is inside the code what will be happend user not aware.