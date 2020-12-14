import art
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

num1 = int(input("What is the frist number: "))
num2 = int(input("What is the second number: "))
for i in operations:
  print(i)

symbol = input("Pick an operation from the list ")
calculation_function = operations[symbol]
answer = calculation_function(num1,num2)

print(f'{num1} {symbol} {num2} = {answer} ')
