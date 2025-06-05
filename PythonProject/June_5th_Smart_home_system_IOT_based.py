#encapsulation - Each devices keeps its internal details (ip,status)
class Devices:
    def __init__(self,name,ip):
        self.name = name
        self.ip = ip
        self.status = "off"

    def turn_on(self):
        self.status = "on"

    def turn_off(self):
        self.status = "off"

#abstraction : UserApp shows only a simple on/off interface
class UserApp:
    def __init__(self):
        self.devices = []

    def add_device(self):
        self.devices.append(Devices)

    def Control_all(self, action):
        for devices in self.devices:
            if action == "on":
                devices.turn_on()
            else :
                devices.turn_off()

#inheritance - inherits devices
class Light (Devices):
    def Control(self,level):
        print(f"Light brightness set to {level}%")

class Fan(Devices):
    def Control(self,speed):
        print(f"Fan speed set to {speed}")

class Ac (Devices):
    def Control(self,Temp):
        print (f"Ac temp set to {Temp} C")

# Polymorphism - Each method behaves differently
devices = {Light("Living Room Light","192.168.1.2"),
            Fan("Celling Fan","192.168.1.3"),
            Ac("Bedroom Ac","192.168.1.4")}

for device in devices:
    device.Control(70)




