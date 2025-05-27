class person:
    def __init__(self,name,age,height,weight,colour):  #constructor
        self.name = name  # Attribute
        self.age = age
        self.height = height   #instance variables unique objects
        self.weight = weight
        self.colour = colour

M1 = person("Manthan",24,165,75,"Asian")
M2 = person("Magan",26,159,70,"Brown")

print(M1.name)
print(M1.age)
print(M1.weight)
print(M1.height)

print(M2.name)
print(M2.age)
print(M2.weight)
print(M2.height)
