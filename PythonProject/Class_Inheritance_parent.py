class parent:
    def __init__(self , FName , LName):
        self.FName=FName;
        self.LName=LName;

#create method for print
    def printname(self):
        print(self.FName,self.LName)

P1 = parent("Sureshbhai","Panchal")

(P1.printname())
print(P1.FName,P1.LName)