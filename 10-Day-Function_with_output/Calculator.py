import art
from replit import clear

print(art.logo)

#addition
def add(n1,n2):
  return n1+n2

#subtraction
def subtract(n1,n2):
  return n2-n1

#multiplication
def multiply(n1,n2):
  return n1*n2

#division
def divide(n1,n2):
  return n1/n2

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}


def calculator():
  num1 = int(input("What is the frist number: "))
  for i in operations: 
    print(i)

  not_continue = False
  while not not_continue:
    symbol = input("Pick an operation from the list ")
    num2 = int(input("What is the second number: "))
    
    calculation_function = operations[symbol]
    answer = calculation_function(num1,num2)
    
    print(f'{num1} {symbol} {num2} = {answer} ')
    if (input("Type 'y' to continue calculation with {answer} and 'n' to start new calculation")=='y'): 
      not_continue = False
      num1=answer()
    else:
      not_continue = True
      clear()
      calculator()


calculator()
