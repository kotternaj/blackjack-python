import random
import os

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = 'J'
        if card == 12: card = 'Q'
        if card == 13: card = 'K'
        if card == 14: card = 'A'
        hand.append(card)
    return hand

def play_again():
    answer = raw_input('Do you want to play again? y/n: ').lower()
    if answer == 'y':
        dealers_hand = []
        players_hand = []
        deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
        game()
    else:
        print 'Bye!'
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == 'J' or card == 'K' or card == 'Q':
            total += 10
        elif:
            if card == 'A':
                if total >= 11 : total += 1
            else: total += 11
        else: total += card
    return total

# def hit(hand):

def clear():
    if os.name == 'nt':
        os.system('CLS')            
    if os.name == 'posix':
        os.system('clear')

# def show_results():

# def blackjack(dealers_hand, players_hand):

# def score(dealers_hand, players_hand):

def game():
    print "Welcome to Python Blackjack"
    players_hand = deal(deck)
    dealers_hand = deal(deck)
    
    print 'Players Hand: %s    Dealers Hand: %s' %(players_hand, dealers_hand)  
 


if __name__ == "__main__":
   game()