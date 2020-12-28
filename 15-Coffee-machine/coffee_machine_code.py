MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_enough(ingredients):
  for item in ingredients:
    if(ingredients[item])>resources[item]:
      print(f'Not enough resources')
      return False
  return True

def is_transaction_successful(payment, cost):
  if(payment >= cost):
    change = round((payment-cost),2)
    print(f'Here is the remaining change ${change}')
    global profit
    profit += cost
    return True
  else:
    print(f'Sorry! Not enough money')
    return False

def pay():
  total = int(input("How many quarter coins? :"))*0.25
  total += int(input("How many dimes? :"))*0.1
  total += int(input("How many nickles? :"))*0.05
  total += int(input("How many pennies? :"))*0.01
  return total

def make_coffee(choice, ingredient):
  for item in ingredient:
    resources[item] = resources[item]-ingredient[item]
  
  print(f'Here  is your {choice} ☕️. Enjoy!')

switch_on = True

while switch_on:
  choice = input("What would you like to have? (espresso/latte/cappuccino):").lower()
  if(choice=='off'):
    switch_on = False
  elif choice == 'report':
    for i in resources:
      print(f'{i}: {resources[i]}')
    print(f'Money: ${profit}')
  else:
    drink = MENU[choice]
    if is_resource_enough(drink['ingredients']):
      payment = pay()
      if is_transaction_successful(payment, drink["cost"]):
        make_coffee(choice, drink['ingredients'])




