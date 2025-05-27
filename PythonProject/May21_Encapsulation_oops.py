class person:
    def __init__(self,name,age):
        self.__name = name    # private attributes
        self.__age = age    #private attributes

    def get_name(self):
        return self.__name   #getter

    def set_age(self,age):   #setter
        if age > 0:
            self.__age = age
        else:
            print("invalid age")

    def show(self):
        print(f"{self.__name} is a {self.__age} years old")

p = person("Manthan",26)
p.show()
print(p.get_name())
p.set_age(9)
p.show()
