
"""
The Game War!!
@author: devinpowers
Lab 10 Part B
"""

import cards

# Create the deck of cards

the_deck = cards.Deck()
# Shuffule the deck
the_deck.shuffle()
print(" =====Shuffled Deck =====")
the_deck.display()


# deal 26 cards to each player (alternating)

print('Dealt 26 cards to each player (alternating')
print()

# create list of cards
player1_list = []
player2_list = []

for i in range(26):
    player1_list.append(the_deck.deal())
    player2_list.append(the_deck.deal())


# display each player's cards all 52 cards have been distributed
print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()


user_selection = input('Would you like to continue?').lower()

winning_player = ""

while user_selection != 'no' and len(player1_list) != 0 and len(player2_list) != 0:
    # player 1 card
    player1_card = player1_list.pop(0)
    print('First Card dealt to player 1:', player1_card)
    
    print('Player 1 hand:', player1_list)
    
    # player 2 card
    player2_card = player2_list.pop(0)
    print('First Card dealt to player 2:', player2_card)
    
    print('Player 2 hand:', player2_list)
    
    # compare ranks of the two cards and decide a winner
    

    
    print()
    if player1_card.rank() == player2_card.rank():
        print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
        player1_list.append(player1_card)
        player2_list.append(player2_card)
    elif player1_card.rank() > player2_card.rank():
        print( "Player #1 wins:", player1_card, "of higher rank than", player2_card )
        winning_player = "Player 1 was the winning player."
        player1_list.append(player1_card)
        player1_list.append(player2_card)
    else:
        print( "Player #2 wins:", player2_card, "of higher rank than", player1_card )
        winning_player = "Player 2 was the winning player."
        player2_list.append(player2_card)
        player2_list.append(player1_card)
    
    # ask if they would like to perform another
    user_selection = input("Would you like to continue?").lower()

print()
print(winning_player)

    
    