from Class_Inheritance_parent import parent


class child(parent):
    def __init__(self, Childname,FName,LName):
        self.Childname = Childname
        #super().__init__(self,FName,LName)



P2 = child("Manthan" , FName="Sureshbhai",LName="Panchal")
#print (P2.Childname)
print (P2.__dict__)




