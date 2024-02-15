from art import logo
import random

print(logo)
list = [1,2,3]
print(list.random.choice())
in_process = True
bidders = {}

def highest_bidder(bidders):
    max_bidder = max(bidders, key=bidders.get)
    max_bid = bidders[find_max_bid]
    print(f"The highest bidder was {max_bidder} with a bid of £    {max_bid}")

  

while in_process:
  name = input("What is your name? ")
  bid = input("What is your bid? ")
  bidders[name] = bid

  
  more_bidders = input("Are there anymore bidders?")
  if more_bidders.lower() == 'no':
    in_process = False
    highest_bidder(bidders)
  elif more_bidders.lower() == 'yes':
    continue
  else:
    print("Invalid, next bidders please")
      