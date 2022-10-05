import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def init_deck():
    ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    for x in range(4):
        for r in ranks:
            deck.append(r)

def deal_dealer():
    x = random.randint(0, len(deck) - 1)
    d_hand.append(deck[x])
    deck.pop(x)

def deal_player():
    x = random.randint(0, len(deck) - 1)
    p_hand.append(deck[x])
    deck.pop(x)


def get_value(hand):
    v = 0
    ace = 0
    for c in hand:
        if isinstance(c, int):
            v += c
        elif c != "A":
            v += 10
        else: 
            ace += 1

    for x in range(ace):
        if v + 11 > 21:
            v += 1
        else: 
            v += 11

    if ace > 0 and v <= 21:
        return (v, True)
    else:
        return (v, False)

def print_hand(hand):
    for x in range(len(hand)):
        if x != len(hand) - 1:
            print(hand[x], end = ", ")
        else:
            print(hand[x], end = " ")
    
    
    
    print("- value:", end = " ")

    v = get_value(hand)

    if v[1] == True:
        print(v[0], " / ", v[0] - 10)
    else:
        print(v[0])

def display_game():
    print("Dealer:")
    print_hand(d_hand)
    print("\nPlayer:")
    print_hand(p_hand)


d_hand = []
p_hand = []
deck = []

def run_game():
    init_deck()
    playing = True
    deal_dealer()
    deal_dealer()
    deal_player()
    deal_player()

    cls()
    display_game()
    if get_value(p_hand)[0] == 21:
        print("\nYou Got BlackJack!!!")
        playing = False

    while playing:
        cls()
        display_game()
        pv = get_value(p_hand)
        dv = get_value(d_hand)

        if pv[0] > 21 or (pv[1] == False and pv[0] > 21):
            print("You Busted!!")
            break
        elif pv[0] < 21:
            while(True):
                d = input("\nWould you like to stand (s) or hit (h)?: ")
                match d:
                    case "s":
                        print("Need to check dealers Hand")
                        playing = False
                        break
                    case "h":
                        deal_player()
                        break
                    case _:
                        print("Error - Incorrect Input, Please try again.")
        else:
            print("You got 21 but need to check dealer")
            break


run_game()




