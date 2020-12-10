import math
def prime_checker(num):
  flag = True
  number = int(math.sqrt(num))
  for i in range(2,number):
    if(number%i==0):
      flag = False

  if(flag == True):
    print(f"{num} is a prime number")  
  else:
    print(f"{num} is not a prime number")

n = int(input("Check this number: "))
prime_checker(num=n)



