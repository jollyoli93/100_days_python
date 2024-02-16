from random import choice
from game_logic import add_cards, twist, win_conditon, dealer_view

cards = {"Ace":11, "Two":2,"Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}
bust = False
player_pot = 1000

#place bet
while not bust:
    bet = input("Place your bets please ")
    print("£" + bet)

    #dealer deals
    players_cards_list = list(cards.keys())
    players_cards = [choice(players_cards_list), choice(players_cards_list)]

    dealers_cards_list = list(cards.keys())
    dealers_cards = [choice(players_cards_list), choice(players_cards_list)]

    #Show Cards
    print(f"Player: {players_cards}")
    print( f"Dealer: {dealers_cards[0]}")

    players_total = add_cards(players_cards, cards)

    print(players_total)

#players turn
    while players_total < 17:
        print("Player must twist")
        players_cards = twist(players_cards, cards)
        players_total = add_cards(players_cards, cards)

    if players_total > 21:
        bust = True
        break

    while True:
        print(f"Players: {players_cards}")
        print( f"Dealers: {dealers_cards[0]}")
        response = input("Stick or Twist? ")

        if response.lower() == "twist":
            print("Player twists")
            players_cards = twist(players_cards, cards)
            players_total = add_cards(players_cards, cards)
            if players_total > 21:
                print(f"{players_total}, player loses")
                bust = True
                break
            elif players_total == 21:
                print("21!")
                break
        elif response.lower() == "stick":
            print("Player sticks")
            bust = True
            break
        else:
            print("Wrong answer, try again")

#dealers turn
            
    dealers_total = add_cards(dealers_cards, cards)
            
    while dealers_total < 17:
        dealers_cards = twist(dealers_cards, cards)
        dealers_total = add_cards(dealers_cards, cards)
        if dealers_total > 21:
            bust = True
        else:
            print("Dealer sticks")
            print(dealers_cards)