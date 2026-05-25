#general practice
# class BankAccount:
#     def __init__(self,name,balance):
#         self.history = []
#         self.name = name
#         self.__balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             self.history.append(f"Deposited {amount}")
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("you dont have enough money")
        
#         elif amount > 0:
#             self.__balance -= amount
#             print(f"{amount} has been deducted from your account")
#             self.history.append(f"Withdrew {amount}")
        
#         else:
#             print("invalid")
    
#     def display_balance(self):
#         return self.__balance  

    
#     def showhistory(self):
#         for transacthistory in self.history:
#             print(transacthistory)

#     def transfer(self,amount,receiver_account):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             self.history.append(f"Transferred {amount} to {receiver_account.name}")

#             receiver_account.deposit(amount)
#             receiver_account.history.append(f"Received {amount} from {self.name}")

#         else:
#             print("invalid")

#=======================================================================================
# #encapsulation practice
# class Account:
#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance
    
#     def withdraw(self,amount):
#         if self.__balance < amount:
#             print("invalid")
        
#         elif self.__balance >= amount:
#             self.__balance -= amount
#             print(f"Withdrew {amount}")
# #logic fix
# class User:
#     def __init__(self,name):
#         self.name = name

# class Admin(User):
#     def delete_user():
#         print("deleted")

# #polymorphism practice
# class Email:
#     def send(self):
#         print("Sending Email notification")


# class SMS:
#     def send(self):
#         print("Sending SMS notification")


# class Push:
#     def send(self):
#         print("Sending Push notification")


# def notify(obj):
#     obj.send()

# #composition practice
# class Engine:
#     def start(self):
#         return "Engine started"


# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def start_car(self):
#         return self.engine.start()

# #class method + static method
# class Math:
#     operation_count = 0

#     @classmethod
#     def increment_operations(cls):
#         cls.operation_count += 1

#     @staticmethod
#     def add(a, b):
#         return a + b

#=======================================================================================
# #polymorphism practice
# class CardPayment:
#     def pay(self):
#         print("payment successful")
# class Cash:
#     def pay(self):
#         print("payment successful")
# class Crypto:
#     def pay(self):
#         print("payment successful")
# class Paypal:
#     def pay(self):
#         print("payment successful")

# #Encapsulation practice
# class BankAccout:
#     def __init__(self,balance):
#         self.__balance = balance

#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"witdrew {amount}")

#         elif amount > self.__balance:
#             print("invalid")
    
#     def deposit(self,amount):
#         if amount <= 0:
#             print("invalid")
#         elif amount > 0:
#             self.__balance += amount
#             print(f"desposit {amount}")

#     def get_balance(self):
#         return self.__balance

# #composition
# class CPU:
#     def start(self):
#         print("CPU running")


# class Computer:
#     def __init__(self):
#         self.cpu = CPU()

#     def turn_on_pc(self):
#         self.cpu.start()
#=======================================================================================
