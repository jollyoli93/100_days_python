from random import choice

def add_cards(card_list, cards):
    total = 0
    for card in card_list:
        total += cards[card]
    return total

def dealer_view(player, dealer):
    for i, card in enumerate(player):
        print(f"player has {card}")
    player_total = add_cards(player)

    for i, card in enumerate(player):
        print(f"Dealer has {dealer[i+1]}")

def twist(deck_input, card_input):
    hand = deck_input
    new_card = list(card_input.keys())
    hand = hand + [choice(new_card)]
    return hand

def win_conditon(player, dealer):
    if player == dealer:
        winner = "draw"
        return winner
    
    elif player > dealer:
        winner = player
        return winner
    
    elif player < dealer:
        winner = dealer
        return winner
     
   