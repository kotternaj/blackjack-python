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
        elif card == 'A':
            if total >= 11 : total += 1
            else: total += 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11 : card == 'J'
    if card == 12: card = 'Q'
    if card == 13: card = 'K'
    if card == 14: card = 'A'
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')            
    if os.name == 'posix':
        os.system('clear')

def show_results(players_hand, dealers_hand):
    clear()
    print 'You have %s for a total of %s ' %(players_hand, total(players_hand))
    print 'The dealer has %s for a total of %s' %(dealers_hand, total(dealers_hand))

def blackjack(dealers_hand, players_hand):
    if total(players_hand) == 21:
        show_results(dealers_hand, players_hand)
        print 'congratulations you got BlackJack!'
        play_again
    elif total(dealers_hand) == 21:
        show_results(dealers_hand, players_hand)
        print 'the dealer got BlackJack!'
        play_again

def score(dealers_hand, players_hand):
    if total(players_hand) == 21:
        show_results(dealers_hand, players_hand)
        print 'congratulations you got BlackJack!'
    elif total(dealers_hand) == 21:
        show_results(dealers_hand, players_hand)
        print 'the dealer got BlackJack!'
    elif total(players_hand) > 21:
        show_results(dealers_hand, players_hand)
        print 'You busted!'
    elif total(dealers_hand) > 21:
        show_results(dealers_hand, players_hand)
        print 'the dealer busted!'  
    elif total(players_hand > dealers_hand):
        show_results(dealers_hand, players_hand)
        print 'You got higher than the dealer! You win!'
    elif total(dealers_hand < players_hand):
        show_results(dealers_hand, players_hand)
        print 'The dealer got higher, he wins!'
        
def game():
    choice = 0
    clear()
    print "Welcome to Python Blackjack /n"
    players_hand = deal(deck)
    dealers_hand = deal(deck)
    while choice != 'q':
        print 'The dealer is showing a %s' %dealers_hand[0]
        print 'You have a %s for a total of %s' %(players_hand, total(players_hand))
        blackjack(players_hand,dealers_hand)
        choice = raw_input('Do you want to [H]it, [S]tand or [Q]uit?: ').lower()
        clear()
        if choice == 'h':
            hit(players_hand)
            while total(dealers_hand < 17):
                hit(dealers_hand)
            score(dealers_hand, players_hand)
            play_again()
        elif choice == 's':
            while total(dealers_hand < 17):
                hit(dealers_hand)
            score(dealers_hand, players_hand)
            play_again()
        elif choice == 'q':
            print 'Bye!'
            quit()

if __name__ == "__main__":
   game()