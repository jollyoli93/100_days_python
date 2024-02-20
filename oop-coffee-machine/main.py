from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

coffee_machine = CoffeeMaker()
payment = MoneyMachine()
menu = Menu()

items = menu.get_items()
ordering = True

while ordering:
    prompt = input(f"Make your selection {items} ")

    if prompt.lower() == "report":
        print(coffee_machine.report())
        print(payment.report())
    else:
        drink = menu.find_drink(prompt)

        resources = coffee_machine.is_resource_sufficient(drink)
        if resources == False:
            ordering = False
            break

        cost_of_drink = drink.cost
        take_payment = payment.make_payment(cost_of_drink)

        if take_payment == True:
            coffee_machine.make_coffee(drink)

        elif take_payment == False:
            ordering = False
