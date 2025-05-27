#base class
from oauthlib.oauth1.rfc5849.signature import verify_hmac_sha1

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started ")

    def show_info(self):
        print(f"Brand : {self.brand} Model : {self.model} Year :  {self.year}")

#Inherited class - car
class Car(Vehicle) :
    def __init__(self,brand,model,year,seats):
        super().__init__(brand,model,year)
        self.seats = seats

    def show_info(self):
        super().show_info()
        print(f"Seats : {self.seats}")

#Inherited class - bike
class Bike(Vehicle):
    def __init__(self,brand,model,year,has_gears):
        super().__init__(brand,model,year)
        self.has_gears = has_gears

    def show_info(self):
        super().show_info()
        print (f"Has Gears : {'yes' if self.has_gears else 'no'}")

#Polymorphism in action
def vehicle_details(vehicle):
    vehicle.show_info()
    vehicle.start_engine()
    print ("-" * 30)

#creating Objects
Car1 = Car("Toyota","Innova",2020,7)
Bike1 = Bike("yamaha","FZ",2022,True)

#using Function to demostrate polymorphism
vehicle_details(Car1)
vehicle_details(Bike1)
