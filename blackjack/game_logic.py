from random import choice

def add_cards(card_list, cards):
    total = 0
    for card in card_list:
        total += cards[card]
    return total

def twist(deck_input, card_input):
    hand = deck_input
    new_card = list(card_input.keys())
    hand = hand + [choice(new_card)]
    return hand

def print_player_cards(player):
        if len(player)<3:
            print(f"Player: {player[0]} | {player[1]}")
        elif len(player) == 3:
            print(f"Player: {player[0]} | {player[1]} | {player[2]}")
        elif len(player) == 4:
            print(f"Player: {player[0]} | {player[1]} | {player[2]} | {player[3]}")

def print_dealer_cards(dealer):
        if len(dealer)<2:
            print(f"Dealer: {dealer[0]}")
        elif len(dealer) == 3:
            print(f"Dealer: {dealer[0]} | {dealer[1]}")
        elif len(dealer) == 4:
            print(f"Dealer: {dealer[0]} | {dealer[1]} | {dealer[2]}")


def win_conditon(player, dealer):
    if player == dealer:
        winner = "draw"

        return winner
    
    elif player > dealer:
        winner = player
        return "Player wins"
    
    elif player < dealer:
        winner = "Dealer wins"
        return winner
     
# def check_ace(card_total):
#     if card_total > 21:
#         if 'Ace' in card_cards:
#             print("Ace is 1")
#             return cards["Ace"] == 1
#         else:
#             print("Player bust!")
#             return bust = True