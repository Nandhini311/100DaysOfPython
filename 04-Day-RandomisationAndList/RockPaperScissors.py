import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_signs = [rock, paper, scissors]
user_choice = int(input("What do you choose? 0-Rock, 1-Paper, 2-Scissors:"))
print(f"user choice: {user_choice}")
computer_choice = random.randint(0,3)
print(f"computer choice: {computer_choice}")

if(user_choice==0 and computer_choice==2):
  print("You win!")
elif(computer_choice>user_choice):
  print("You loose!")
elif(computer_choice == user_choice):
  print("It's a Draw!")
else:
  print("You typed an invalid number! You loose honey")
