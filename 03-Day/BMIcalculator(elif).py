#Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.

bmi = round(weight/height**2)

if(bmi<18.5):
  print(f"Your bmi is {bmi} ! you are underweight")
elif(bmi<25):
  print(f"Your bmi is {bmi} ! you are normal weight")
elif(bmi<30):
  print(f"Your bmi is {bmi} ! you are slightly overweight")
elif(bmi<35):
  print(f"Your bmi is {bmi} ! you are obese")
else:
  print(f"Your bmi is {bmi} ! you are clinically obese")
