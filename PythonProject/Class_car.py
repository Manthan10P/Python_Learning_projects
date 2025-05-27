from plistlib import readPlist
from tokenize import Single3


class car :
    def __init__(self, brand , colour , carname ):
        self.brand = brand;
        self.colour = colour;
        self.carname = carname;

S1 = car("Maruti","Black","Fronx")
S2 = car ("Nissan","White","Magnite")
S3 = car ("Skoda","Brown","Octiva")


print(S1.brand)
print(S1.colour)
print(S1.carname)
print(S1.brand,S1.colour,S1.carname)
print(S1)

print(S2.brand)
print(S2.colour)
print(S2.carname)
print(S2.brand,S2.colour,S2.carname)
print(S2)

print(S3.brand)
print(S3.colour)
print(S3.carname)
print(S3.brand,S3.colour,S3.carname)
print(S3)