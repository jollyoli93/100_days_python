from random import choice
from game_logic import add_cards, twist, win_conditon, print_player_cards

cards = {"Ace":11, "Two":2,"Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}

player_pot = 1000
game_over = False
#place bet
while not game_over:
    start_game = input("Press enter to play or no to quit: ")
    print(start_game)

    if player_pot == 0:
        game_over = True
        break
    elif start_game.lower() =='no':
        game_over = True
        break

    bust = False
    bet = input("Place your bets please ")
    player_pot -= bet
    print("£" + bet)

    #dealer deals
    players_cards_list = list(cards.keys())
    players_cards = [choice(players_cards_list), choice(players_cards_list)]

    dealers_cards_list = list(cards.keys())
    dealers_cards = [choice(players_cards_list), choice(players_cards_list)]

    #Show Cards
    print("Dealer deals the cards")
    print_player_cards(players_cards)
    print( f"Dealer: {dealers_cards[0]}")

    players_total = add_cards(players_cards, cards)

    print(players_total)

    #players turn
    while players_total < 17:
        print(input("Player must twist, press to continue"))
        players_cards = twist(players_cards, cards)
        players_total = add_cards(players_cards, cards)
        print_player_cards(players_cards)

    if players_total > 21:
        print("Player bust!")
        print_player_cards(players_cards)
        break

    while not bust:
        response = input("Stick or Twist? ")

        if response.lower() == "twist":
            print("Player twists")
            players_cards = twist(players_cards, cards)
            players_total = add_cards(players_cards, cards)
            print_player_cards(players_cards)

            if players_total > 21:
                print(f"{players_total}, player loses")
                print_player_cards(players_cards)

                bust = True
                break
            elif players_total == 21:
                print("21!")
                break
        elif response.lower() == "stick":
            print("Player sticks")
            break
        else:
            print("Wrong answer, try again")

    #dealers turn
    
    if not bust:
        print("Dealers turn")
        print(f"Dealer: {dealers_cards[0]}, {dealers_cards[1]}")
        dealers_total = add_cards(dealers_cards, cards)
                
        while dealers_total < 17:
            dealers_cards = twist(dealers_cards, cards)
            dealers_total = add_cards(dealers_cards, cards)
            print( f"Dealer: {dealers_cards[0]}, {dealers_cards[1]}, {dealers_cards[2]}")

            if dealers_total > 21:
                bust = True
                break
            else:
                print("Dealer sticks")
                print(dealers_cards)
                break

        #check winners
        winner = win_conditon(players_total, dealers_total)
        print(winner)