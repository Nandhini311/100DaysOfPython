#You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = len(names)
intnum = random.randint(0,x-1)
print(names[intnum])

#****************************************

person = random.choice(names)
print(person)
