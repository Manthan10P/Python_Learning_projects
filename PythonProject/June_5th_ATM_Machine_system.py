#encapsulation - sensitive details like __pin and __balance are kept private
from future.utils import reraise


class Account:
    def __init__(self,acc_no,pin,balance=0):
        self.acc_no = acc_no
        self.pin = pin
        self.__balance = float(balance)

    def check_pin(self,entered_pin):
        return self.__pin == entered_pin

    def get_balance(self):
        return self.__balance

    def deposite(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

#abstraction - ATM interfaces only shows buttons not internal logic
class ATM :
    def access_amount(self,account,pin):
        if account.check_pin(pin):
            print("Account Access Granted")
            return True
        else:
            print("Invalid Pin")
            return False

#inheritance - Two types of account inherits from account
class SavingsAccount(Account):
    def calculate_interest(self):
        return self.get_balance() * 0.04

class CurrentAccount(Account):
    def calculate_interest(self):
        return 0  #usually no interest

#polymorphism - same method calculate interest() behaves differently
accounts = [SavingsAccount("001","123","100000"),CurrentAccount("101","5678","500000")]

print(f"Balance: ₹{accounts[0].get_balance()}")
print(f"Interest: ₹{accounts[0].calculate_interest()}")
print(f"Balance: ₹{accounts[1].get_balance()}")
print(f"Interest: ₹{accounts[1].calculate_interest()}")




