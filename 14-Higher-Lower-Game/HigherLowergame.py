import art
from game_data import data
import random 
from replit import clear

print(art.logo)


def random_account():
  return random.choice(data)

def format_account(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  
  return f"{name},a {description}, from {country}"

def check_answer(guess,a_follower,b_follower):
  if a_follower > b_follower:
    return guess == 'a'
  else: return guess == 'b'
  
def game():
  print(art.logo)
  score = 0
  game_should_continue = True
  account_a = random_account()
  account_b = random_account()


  while game_should_continue:
    account_a = account_b
    account_b = random_account()

  while account_a == account_b:
    account_b = random_account()

  print(f"Compare A: {format_account(account_a)}.")
  print(art.vs)
  print(f"Against B: {format_account(account_b)}.")

  guess = input("Who has more number of followers: ")
  a_follower = account_a["follower_count"]
  b_follower = account_b["follower_count"]
  is_correct = check_answer(guess,a_follower,b_follower)
  
  clear()
  if is_correct:
    score = score+1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")

  
game()
