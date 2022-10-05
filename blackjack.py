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
    print(x)
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

    if ace == 1:
        return (v, True)
    else:
        return (v, False)

def print_player_hand():
    for x in range(len(p_hand)):
        if x != len(p_hand) - 1:
            print(p_hand[x], end = ", ")
        else:
            print(p_hand[x], end = " ")
    
    
    
    print("- value:", end = " ")

    v = get_value(p_hand)

    if v[1] == True:
        print(v[0], " / ", v[0] - 10)
    else:
        print(v[0])

def print_dealer_hand():
    print(d_hand[0])

def print_hand(hand):
    for x in range(len(hand)):
        if x != len(hand) - 1:
            print(hand[x], end = ", ")
        else:
            print(hand[x], end = " ")

    print("- value:", end = " ")

    v = get_value(hand)
    print(v[0])

def display_game():
    print("Dealer:")
    print_dealer_hand()
    print("\nPlayer:")
    print_player_hand()

def determine_outcome():
    cls()
    print("Dealer:")
    print_hand(d_hand)
    print("\nPlayer:")
    print_hand(p_hand)
    print("")

    dv = get_value(d_hand)[0]
    pv = get_value(p_hand)[0]

    if dv > 21:
        print("Dealer Busted!! You WIN!")
    elif dv > pv:
        print("Dealer has a higher value hand!! You LOST!")
    elif dv < pv:
        print("Dealer has a lower value hand!! You WON!")
    else:
        print("You had same value hand as the dealer!! You tied!")


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

        if pv[0] > 21 or (not pv[1] and pv[0] > 21):
            print("You Busted!!")
            break
        elif pv[0] < 21:
            while(True):
                d = input("\nWould you like to stand (s) or hit (h)?: ")
                match d:
                    case "s":
                        while(True):
                            dv = get_value(d_hand)[0]
                            if dv <= 16:
                                deal_dealer()
                            else:
                                determine_outcome()
                                break
                        playing = False
                        break
                    case "h":
                        deal_player()
                        break
                    case _:
                        print("Error - Incorrect Input, Please try again.")
        else:
            determine_outcome()
            break


run_game()




