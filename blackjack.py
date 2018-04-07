import random
import os

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffl(deck)
        card = deck.pop()
        if card == 11: card = 'J'
        if card == 12: card = 'Q'
        if card == 12: card = 'K'
        if card == 12: card = 'A'
        hand.append(card)
    return hand

def play_again():

def total(hand):

def hit(hand):

def clear():
    if os.name == 'nt':
        os.system('CLS')            
    if os.name == 'posix':
        os.system('clear')

def show_results():

def blackjack(dealers_hand, players_hand):

def score(dealers_hand, players_hand):

def game():

