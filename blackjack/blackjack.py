from random import choice
from game_logic import add_cards, twist, win_conditon, print_player_cards, print_dealer_cards

def play_game():
    cards = {"Ace":11, "Two":2,"Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}
    player_pot = 1000
    game_over = False

    while not game_over:
        start_game = input("Press enter to play or no to quit: ")
        print(start_game)

        if player_pot <= 0:
            game_over = True
            return "Out of money, go home!"
        elif start_game.lower() =='no':
            game_over = True
            return "End of game"

        bust = False

        while True:
            print("Place your bets please:")
            bet = input("£")

            if bet.isdigit():
                player_pot = player_pot - int(bet)
                break
            else:
                print("Enter a correct number")

        print("\
                ")    
        #DEBUG
        #dealer deals
        cards_list = list(cards.keys())
        players_cards = [choice(cards_list), choice(cards_list)]

        dealers_cards = [choice(cards_list)]

        #Show Cards
        print("Dealer deals the cards")
        print("\
                ")    
        
        print_player_cards(players_cards)
        print_dealer_cards(dealers_cards)
        players_total = add_cards(players_cards, cards)

        #players turn
        while players_total < 17:
            print(input("Player must twist, press to continue"))
            players_cards = twist(players_cards, cards)
            players_total = add_cards(players_cards, cards)            
            print_player_cards(players_cards)

        if players_total > 21:
            if 'Ace' in players_cards:
                print("Ace is 1")
                cards["Ace"] == 1
            else:
                print("Player bust!")
                bust = True

        while not bust:
            response = input("Stick or Twist? ")
            print("\
                ")

            if response.lower() == "twist":
                print("Player twists")
                print("\
                    ")            
                players_cards = twist(players_cards, cards)
                players_total = add_cards(players_cards, cards)
                print_player_cards(players_cards)

                if players_total > 21:
                    if 'Ace' in players_cards:
                        print("Ace is 1")
                        cards["Ace"] == 1
                        continue
                    else:
                        print(f"{players_total}, player loses")
                        bust = True
                        break
                elif players_total == 21:
                    print("21!")
                    break

            elif response.lower() == "stick":
                print("Player sticks")
                print("\
                    ")            
                break
            else:
                print("Wrong answer, try again")
                print("\
                    ")            

        #dealers turn
        
        if not bust:
            cards["Ace"] == 11

            print("Dealers turn")
            print("\
                ")
            dealers_total = add_cards(dealers_cards, cards)
            print_dealer_cards(dealers_cards)
                    
            while dealers_total < 17:
                dealers_cards = twist(dealers_cards, cards)
                dealers_total = add_cards(dealers_cards, cards)
                print_dealer_cards(dealers_cards)
                print("\
                    ")            

            if dealers_total > 21:
                if 'Ace' in dealers_cards:
                    cards["Ace"] == 1
                    dealers_cards = twist(dealers_cards, cards)
                else:
                    print("Player bust!")
                    bust = True
            else:
                print("Dealer sticks")
                print_dealer_cards(dealers_cards)
                print("\
                    ")
        #check winners
        if not bust:
            winner = win_conditon(players_total, dealers_total)
            print(winner)

print(play_game())