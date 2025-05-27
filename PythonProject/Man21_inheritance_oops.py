class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"{self.name},{self.age}")

class student(person):
    def __init__(self,name,age,studentid,course):
        super().__init__(name, age)
        self.studentid = studentid
        self.course = course

    def show_student(self):
        print(f"{self.name},{self.age},{self.studentid},{self.course}")

class professor(person):
    def __init__(self,name,age,employid,subject):
        super().__init__(name, age)
        self.employid = employid
        self.subject = subject

    def show_professor(self):
        print(f"{self.name},{self.age},{self.employid},{self.subject}")


M1 = person("Mrugesh",28)
M2 = student("vishal",22,"S101","Electronics")
M3 = professor("mrudang",35,"P12","Communication")

M1.show_person()
M2.show_student()
M3.show_professor()