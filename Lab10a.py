#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:06:52 2020

@author: devinpowers
"""


##
## Demonstrate some of the operations of the Deck and Card classes
##

import cards

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).

import random
random.seed( 100 )

# Create a deck of cards

my_deck = cards.Deck()


# Shuffle the deck, then display it in 13 columns

my_deck.shuffle()
print( "===== shuffled deck =====" )
my_deck.display()


# Deal five cards to each player (alternating)

print( "Dealt five cards to each player (alternating)" )
print()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( my_deck.deal() )
    player2_list.append( my_deck.deal() )

# Display each player's cards and the cards still in the deck

print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()
print( "===== remaining cards in deck =====" )
my_deck.display()








# Function for handling each time a card is drawn

def hand(index, hand_name):

    # First card dealt to Player #1
    print('\n')
    # pop first element from the list
    player1_card = player1_list.pop(index)
    
    print( "First card dealt to player #1:", player1_card )
    # Display hand after card has been played
    print('Player # 1 Hand', player1_list)
    

    # First card dealt to Player #2
    print()
    player2_card = player2_list.pop( index )
    print( "First card dealt to player #2:", player2_card )
    print('Player # 2 Hand', player2_list)

    # Compare the ranks of the two cards
    print()
    if player1_card.rank() == player2_card.rank():
        print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
    elif player1_card.rank() > player2_card.rank():
        print( "Player #1 wins:", player1_card, "of higher rank than", player2_card )
    else:
        print( "Player #2 wins:", player2_card, "of higher rank than", player1_card )


# First Hand
hand(0, 'First')

#Second Hand
hand(0, 'Second')

# Last Hand
hand(-1, 'Last')