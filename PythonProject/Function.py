def my_function():
    print("Called Function")

my_function()

def my_func(Name):
    print(Name +" "+ "Panchal")

my_func("Sureshbhai")
my_func("Manthan")
my_func("Anitaben")
my_func("Pooja")

#Arbitrary Arguments, *args
def child( * kids):
    print("Youngest Child " + kids[1])

child("Manthan","Dev","Sahil")

#Keyword Arguments
def Family (child3 , child1 , child2):
    print(child2)
    print(child1)
    print(child3)
Family (child1="Manthan",child2="Dev",child3="Sahil")

#Default Parameter Value
def info (country = "india"):
    print("i am from "+ " " + country)

info("Norway")
info("USA")
info("UK")
info()

#Passing a List as an Argument
def my_fruit(food):
    for i in food:
        print(i)
fruit = ['Banana','Mango','cherry']
my_fruit(fruit)

#Return Values
def calculate(x):
    return 5 * x

print(calculate(6))
print(calculate(55))
print (calculate(45))


