class person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def Myfunc(self):
        print("Hello How are you " + self.name)

P1 = person("john" , 36)

print(P1.name,P1.age)
P1.Myfunc()
