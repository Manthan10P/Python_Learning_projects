from aptdaemon.worker.aptworker import read_high_trust_repository_dir
from reportlab.rl_settings import autoGenerateMissingTTFName

class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} {self.price}")

class VegItem(MenuItem):
    def __init__(self,name,price):
        super().__init__(name,price)
        self.type = "Vegetarian"

class NonVegItem(MenuItem):
    def __init__(self,name,price):
        super().__init__(name,price)
        self.type = "Non-vegetarian"

class restaurant:
    def __init__(self,name):
        self.name = name
        self.menu = []

    def add_item_to_menu(self,item):
        self.menu.append(item)

    def display_menu(self):
        print(f"/n----{self.name} menu -----")
        for item in self.menu:
            item.display()

class user :
    def __init__(self,name):
        self.name = name
        self.orders = []

    def place_order(self,restaurant,item_names):
        items = [item for item in restaurant.menu if item.name in item_names]
        order = Order(self,items)
        self.orders.append(order)
        return order

class Order:
    __id_counter = 1

    def __init__(self,user,items):
        self.__order_id = Order.__id_counter
        Order.__id_counter +=1
        self.user = user
        self.items = items
        self.total = sum(item.price for item in items)

    def display_order(self):
        print(f'/n Order ID : {self.__order_id} /n Customer : {self.user.name}')
        for item in self.items:
            print(f"-{item.name}({item.price}")
        print(f'Total : ${self.total}')

class DeliveryAgent:
    def __init__(self,name):
        self.name = name

    def deliver_order(self,order):
        print(f"/n DelieryAgent {self.name} is delivering order ID {order._Order__order_id} to {order.user.name}...")

#----------------------------sample usage-----------------------------------------------
if __name__ == "__main__":
    #for restaurant and menu
    dominos = restaurant("Dominos")
    dominos.add_item_to_menu(VegItem("Margrita",199))
    dominos.add_item_to_menu(NonVegItem("Chicken",299))

# create user
    user1 = user("Manthan")

#show menu and place order
    dominos.display_menu()
    order1 = user1.place_order(dominos,["margrita","chicken"])
    order1.display_order()

#deliver order
    agent = DeliveryAgent("Rahul")
    agent.deliver_order(order1)








