class Mobile:           #method overriding
    def turn_on(self):
        print ("Mobile is Turning ON")

class Laptop:
    def turn_on(self):
        print("Laptop is Turning ON")

class Vehical:
    def turn_on(self):
        print("Vehical is Turning ON")

devices = [Mobile(),Laptop() ,Vehical()]

for device in devices:
    device.turn_on()

