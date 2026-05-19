# #functions?+++++++++++++++++
# def say_hello():
#     print("hello")

# sheesh = say_hello

# sheesh

#  HIGHER ORDER FUNCTIONS+++++++++++++++++
# #function using another function
# def add(a, b):
#     c = a + b
#     return c

# def execute(add):
#     return add(2,3)

# print(execute(add))

# #closures wrapper concept+++++++++++++++++
# # A function that remembers variables from its outer function
# # even after the outer function has finished running. That “memory” is the closure.
# # Each function carries its own “saved state” used in caching.

# def multiplier(n):
#     def multiply(x):
#         return x * n
#     return multiply

# double = multiplier(2)
# print(double(5))

# triple = multiplier(3)
# print(triple(5))

# #decorators+++++++++++++++++

# current_user = {"logged_in": True}

# def login_required(func):
#     def wrapper():
#         if not current_user["logged_in"]:
#             print("Access denied")
#             return
#         return func()
#     return wrapper

# @login_required #this is the decorator
# def view_profile():
#     print("Profile data")

# view_profile()

# #what the helly is this "@"
# """
# @login_required
# def view_profile():
#     print("Profile data")
# """

# """

#     it just kinda adds or modify the function below? it basically says run this function login
#     before running the code below

#     Real-world analogy
#     Function = room you want to enter
#     Decorator = security guard at the door
#     Guard decides:
#     let you in (run function)
#     or block you

# """

#practice
#higher order functions
# def say_hello():
#     return print("halo")

# x = say_hello

# print(x())

#closures
# def counter():
#     count = 0

#     def add():
#         nonlocal count
#         count += 1
#         print(count)

#     return add

# c = counter
# c()
# c()
# c()

# #decorator
# def sheesh(func):
#     def krezy():
#         print("hmmmmmmm")
#         func()
#         print("kkkkkkk")
#     return krezy

# @sheesh
# def hello():
#     print("hello")

# hello()

# #LOGIN DECORATOR (AUTH SYSTEM)
# current_user = {
#     "username" : "kurumi",
#     "logged_in" : True
# }

# def login_required(func):
#     def wrapper(*args,**kwargs):
#         if not current_user["logged_in"]:
#             print("access denied: user not logged in")
#             return
#         return func(*args,**kwargs)
#     return wrapper

# @login_required
# def view_dashboard():
#     print("Welcome to dashboard")

# #LOGGING DECORATOR (BACKEND MONITORING)
# def log_function(func):
#     def wrapper(*args, **kwargs):
#         print(f"[LOG] Function '{func.__name__}' is starting")
#         result = func(*args, **kwargs)
#         print(f"[LOG] Function '{func.__name__}' finished")
#         return result
#     return wrapper

# @log_function
# def deposit(amount):
#     print(f"Depositing {amount}")

# #VALIDATION DECORATOR (INPUT SECURITY
# def validate_amount(func):
#     def wrapper(amount, *args, **kwargs):
#         if amount <= 0:
#             print("Invalid amount: must be > 0")
#             return
#         return func(amount, *args, **kwargs)
#     return wrapper

# @validate_amount
# def withdraw(amount):
#     print(f"Withdrawing {amount}")

# #COMBINING DECORATORS
# @log_function
# @validate_amount
# def transfer(amount):
#     print(f"Transferring {amount}")

# current_user["logged_in"] = True
# view_dashboard()

# transfer(500)
# transfer(-50)

# current_user["logged_in"] = False
# view_dashboard()


# def simple_decorator(func):
#     def starter():
#         print(f"[LOG] BEFORE {func.__name__}")
#         func()
#         print(f"[LOG] AFTER {func.__name__}")
#     return starter
    

# @simple_decorator
# def hello():
#     print("hello world")

# hello()

# def multiplier(n):
#     def multiply(x):
#         return n * x
#     return multiply

# double = multiplier(2)
# triple = multiplier(3)

# print(double(5))  # 10
# print(triple(5))  # 15

# def count():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         print(count)
#     return counter

# c = count()
# c()
# c()
# c()