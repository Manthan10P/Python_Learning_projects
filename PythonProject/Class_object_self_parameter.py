class person:
    def __init__(Silyobject, name, age):
        Silyobject.name = name;
        Silyobject.age = age;

    def Myfunc(Object):
        print("Hello How are you " + Object.name)

P1 = person("Manthan" , 36)
##self replace with different name
print(P1.name,P1.age)
P1.Myfunc()

#Modify Object Properties
#you can modify properties on object
P1.age = 40
print(P1.age)

