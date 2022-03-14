from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    selection = input(f"What would you like? ({menu.get_items()}) ").lower()
    if selection == "off":
        is_on = False
    elif selection == "report":
        coffee_machine.report()
        money.report()
    else:
        item = menu.find_drink(selection)
        if item and coffee_machine.is_resource_sufficient(item) and money.make_payment(item.cost):
            coffee_machine.make_coffee(item)