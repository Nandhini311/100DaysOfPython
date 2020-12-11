from replit import clear #to clear the output in your console

bid_details = {}

def get_max_bid(bid_details):
  maximum = 0
  for i in bid_details:
    if(bid_details[i] > maximum):
      name = i
      maximum = bid_details[i]

  clear()

  print(f"The winner is {name} with bidding amount ${maximum}")
end_values = False

while not end_values:
  name = input("What is your name? : ")
  bid = int(input("What is you bid? : $"))
  bid_details[name]=bid
  any_more = input("Are there any others bidder? : ").lower()
  if any_more == 'no':
    end_values = True
    print("Thanks for bidding")
    get_max_bid(bid_details)
  else:
    clear()
