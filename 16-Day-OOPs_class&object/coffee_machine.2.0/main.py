from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
my_menu = Menu()

is_on = True

while is_on:
    option = my_menu.get_items()
    user_choice = input(f"Choose one from the menu ({option}): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffe_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(user_choice)
        if coffe_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
        