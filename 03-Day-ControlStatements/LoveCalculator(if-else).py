print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1+name2
combined_name.lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
n1 = t+r+u+e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
n2 = l+o+v+e

love = str(n1)+str(n2)
love = int(love)
if love < 10 or love > 90:
  print(f"Your score is {love}% , you go together like coke and mentos")
elif love > 40 and love < 50:
  print(f"Your score is {love}% , you are alright together")
else: print(f"Your score is {love}% ")
