from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            payment = money.make_payment(drink.cost)
            if payment:
                coffee.make_coffee(drink)

# Course Code
def course():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()
    is_on = True

    money_machine.report()
    coffee_maker.report()

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
