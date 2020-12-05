#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("Enter the bill amount: $"))
tip_per = int(input("Enter the tip percent 10/12/15%: "))
num = int(input("Enter the number of people: "))

tip = tip_per/100
amount = (bill/num)*(1+tip)
final_amount = "{:.2f}".format(amount)

print(f"Each person should pay: ${final_amount}")
