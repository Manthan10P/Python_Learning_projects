class Flight:
    def __init__(self,flight_no,origin,destination,base_price):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.base_price = base_price

    def calculate_price(self,seat_class):
        return self.base_price  #to be overriden

class DomesticFlight(Flight):
    def calculate_price(self,seat_class):
        if seat_class == "Business" :
            return self.base_price * 1.5
        return self.base_price

class InternationalFlight(Flight):
    def calculate_price(self,seat_class):
        if seat_class == "Business" :
            return self.base_price * 2
        return self.base_price * 1.2

class Passenger:
    def __init__(self,name,passport=None):
        self.name = name
        self.passport = passport

class Ticket:
    __pnr_counter = 1001  #private encapsulated

    def __init__(self,passenger,flight,seat_class):
        self.passenger = passenger
        self.flight = flight
        self.seat_class = seat_class
        self.__pnr = Ticket.__pnr_counter
        self.__pnr_counter +=1
        self.price = flight.calculate_price(seat_class)

    def display_ticket(self):
        print(f"Ticket PNR {self.__pnr}")
        print(f"passenger {self.passenger}")
        print (f"Flight NO {self.flight.flight_no}")
        print (f"From : {self.flight.origin} to {self.flight.destination}")
        print (f"Class {self.seat_class} | Price: ${self.price}")

class Airline:
    def __init__(self,name):
        self.name = name
        self.flight = []

    def add_flight(self,flight):
        self.flight.append(flight)

    def show_flight(self):
        print(f"/n {self.name} flight")
        for flight in self.flight:
            print (f"{flight.flight_no} {flight.origin} -> {flight.destination} (base: ${flight.base_price})")

#--------------------------sample usage --------------------------
if __name__ == "__main__":
    #create AIrline
    airindia = Airline("airindia")

    #add flight
    airindia.add_flight(DomesticFlight("A101","Delhi","Mumbai",3000))
    airindia.add_flight(InternationalFlight("M101","Australia","US", 8000))
    airindia.add_flight(DomesticFlight("A102", "Ahmedabad", "Jaipur", 5000))
    airindia.add_flight(InternationalFlight("M102", "London", "Newzland", 10000))

    #show flight
    airindia.show_flight()

    #book ticket
    passenger1 = Passenger("Manthan",passport="M1234567890")
    selected_flight = airindia.flight[0]
    ticket1 = Ticket(passenger1,selected_flight,"Business")
    ticket1.display_ticket()
