# Python Program to Check Leap Year using If Statement
#it should be divisible by 4 or 400 and not be divisible by 100, for it to be a leap year

year = int(input("Please Enter the Year Number you wish: "))

if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
    
#incase of elif any one of the statement will be executed and multiple if any number of the statement can be executed if condition is satisifed
