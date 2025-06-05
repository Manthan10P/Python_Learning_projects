class Doctor:
    def __init__(self,name,specialization):
        self.name = name
        self.specialization = specialization

    def treat_patient(self):
        print (f"Dr.{self.name} is treating a patient")

#inherited class
class Surgeon (Doctor):
    def treat_patient(self):
        print(f"Dr.{self.name} is a performing a surgery")

class Dentist(Doctor):
    def treat_patient(self):
        print (f"Dr.{self.name} is doing a dental check-up")

class Pediatrician(Doctor):
    def treat_patient(self):
        print(f"Dr.{self.name} is treating a child")

#patient class
class Patient:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__medical_history = []

    def add_history(self,record):
        self.__medical_history.append(record)

    def get_history(self):
        return self.__medical_history

#Appointment class

class Appointment :
    def __init__(self,doctor,Patient,time_slot):
        self.doctor = doctor
        self.Patient = Patient
        self.time_slot = time_slot

    def Confirm(self):
        print(f"Appointment confirm with Dr.{self.doctor.name} at {self.time_slot} for {self.Patient.name}")
        self.doctor.treat_patient()

#sample flow
doc1 = Surgeon("sharma" , "Surgery")
doc2 = Dentist("Kapoor","Dentist")
doc3 = Pediatrician("Valand","Pediatrician")

Pat1 = Patient("Maheta",45)
Pat2 = Patient ("Agrawal",61)
Pat3 = Patient ("Singaniya",10)

appointment1 = Appointment(doc1,Pat1,"10:30 AM")
appointment1.Confirm()
appointment2 = Appointment(doc2,Pat2,"08:30 PM")
appointment2.Confirm()
appointment3 = Appointment(doc3,Pat3,"02:30 PM")
appointment3.Confirm()



