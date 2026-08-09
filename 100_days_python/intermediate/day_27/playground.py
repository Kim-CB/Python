# Advanced Arguments

# Arguments with Default Values
# def my_function(a=1, b=2, c=3):
#   Do this with a 
#   Then do this with b
#   Finally do this with c
# i can change on calling the function
# my_function(4,5) -> changes to a=4 and b=5

# Unlimited Arguments - aldo know as unlimeted positional arguments
# def add(*args):
#   for n in args:
#       print(n)
# the * tells python the function can accept any number of arguments, like add(4,5,6,7)
def add(*args):
    soma = [n for n in args]
    print(sum(soma))
#add(5,5,20,3,6)

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
#calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)