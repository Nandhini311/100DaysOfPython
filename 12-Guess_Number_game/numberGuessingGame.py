import random 
import art 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#check user's answer against actual answer
def checkguess(guess,num2guess,turn):
  if(guess>num2guess):
    print("Too high")
    return turn-1
  elif(guess<num2guess):
    print("Too low")
    return turn-1
  else:
    print(f"Bingo you got it right {num2guess}")

#setting difficutly
def difficulty():
  level = input("Choose difficulty, easy or hard").lower()
  if(level== "easy"):
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


#choosing random number between 1 to 100
def game():
  print(art.logo)
  print('''Welcome to the guessing game
  I am thinking of a number between 1 to 100''')
  num2guess = random.randint(1,100)
  turn = difficulty()

  guess = 0
  #let the user guess a number
  while guess!=num2guess:
    print(f"you have {turn} attempts to make remaining attempt")

    guess = int(input("Make a guess: "))

    turn = checkguess(guess, num2guess, turn)
    if turn == 0:
      print(f"You've run out of guesses, you lose. The correct guess is {num2guess}")
      return
    elif guess != num2guess:
      print("Guess again.")
    


game()
