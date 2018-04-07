import random

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffl(deck)
        card = deck.pop()
        if  