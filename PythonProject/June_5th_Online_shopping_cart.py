class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = float(price)

    def Apply_discount(self):
        return self.price   #default no discount

class Electronics(Product):
    def Apply_discount(self):
        return self.price * 0.90 #10% off

class Clothings(Product):
    def Apply_discount(self):
        return self.price * 0.80 #20% off

class Grocery(Product):
    def Apply_discount(self):
        return self.price * 0.95

#cart class
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self,product):
        self.items.append(product)
        print(f"{product.name} added to cart")

    def total(self):
        return sum(item.Apply_discount() for item in self.items)

#user class
class User:
    def __init__(self,name):
        self.name = name
        self.cart = Cart()

#payment with encapsulation
class Payment:
    def __init__(self,Card_number):
        self.__Card_number = Card_number  #encapsulated

    def Process_payment(self,amount):
        print(f"Processing ${amount :.2f} from card ending with {str(self.__Card_number)[-4:]}")

# demo flow
# create user
user1 = User("Manthan")

#add product
phone = Electronics("iPhone","80000")
shirt = Clothings ("T-shirt",1500)
milk = Grocery ("Milk","50")

user1.cart.add_product(phone)
user1.cart.add_product(shirt)
user1.cart.add_product(milk)

#checkout
total_amount = user1.cart.total()
print(f"Total after discount : {total_amount : 0.2f}")

#pay
payment = Payment("1234 5678 9010")
payment.Process_payment(total_amount)
        
