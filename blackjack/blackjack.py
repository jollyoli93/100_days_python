from random import choice
from game_logic import add_cards

cards = {"Ace":11, "Two":2,"Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}
#place bet
bet = input("Place your bets please ")
print("£" + bet)

#dealer deals
players_cards_list = list(cards.keys())
players_cards = [choice(players_cards_list), choice(players_cards_list)]

dealers_cards_list = list(cards.keys())
dealers_cards = [choice(players_cards_list), choice(players_cards_list)]

#Show Cards
print(players_cards, dealers_cards[0])

#check if cards under 17, if so must hit, elif < 17 hit or stick
players_total = add_cards(players_cards, cards)
print(players_total)

if players_total < 17:
    twist()
if players_total > 17:
    response = input("Stick or Twist? ")
else:
    stick()

#check if >21 then bust
#if <21, hit or twist?
#if >21 bust, elif dealer == player, draw. elif player > dealer, win. else, lose.\\wsl.localhost\Ubuntu\home\jollyoli93\python_projects