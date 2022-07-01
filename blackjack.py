#!/usr/bin/python

import random

import getpass

import time

#deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", "Ace", "Ace", "Ace", "Ace", "Ace", "Ace", "Ace", "Ace"]

deck52 = deck *4

wallet = 100

# dealer = []

# player = []

# aceplayer = []

# acedealer = []

def givevalue(card):
    """
    Returns how many gives a card

    Args:
        card: int ou str

    Return:
        integer: amount of points
    """    

    if type(card) == int:
        return card

    if type(card) == str and card != "Ace":
        return 10

    if card == "Ace":
        return 0

#comment faire avec un seul argument (hand) puis ace[hand]??
def total(hand, acehand):
    """
    Returns total number of points in a player's hand

    Args:
        hand(list): player's or dealer's hand

    Return:
        integer: total amount of points
    """
    total = 0
    totalace = 0
    for card in hand:
        total = total + givevalue(card)
    if hand.count("Ace") >= 1:
        for ace in acehand:
            totalace = totalace + ace
    return total + totalace
  

def styled(hand):
    """
    Displays cards of a deck in a stylized way 

    Args:
        hand(list): player's or dealer's hand

    Return:
        string: < card1 >, < card2 >, etc. 
    """
    styled = []
    for card in hand:
        style = f"< {card} > "
        styled.append(style)
    return " ".join(styled)


def takecard(hand):
    """
    takes a random card from the deck and adds it to the list "player"

    Args:
        player: defines which hand will be updated (player or dealer's)
    """
    card = random.choice(deck52)
    hand.append(card)
    deck52.remove(card)

#*************************************
#****************JEU******************
#*************************************

print(f"\nWelcome {getpass.getuser()}\n")

time.sleep(2)

print("You have 100$.")

replay = "y"

while wallet > 0:

    if replay == "y":

        dealer = []

        player = []

        aceplayer = []

        acedealer = []

        bet = int(input("\nHow much do yo wish to bet?\n"))

        wallet = wallet - bet

        #************************************
        #**********MAINS DE DEPART***********
        #************************************
        print("\nLet's look at the hands...\n")

        time.sleep(2)

        #voir pour faire fonction takecard avec 2 args où 2ème serait nombre d'itérations
        for required in range(2):
            takecard(dealer)

        print(f"Dealer:\n< ? >  < {dealer[-1]} >")

        #*********choix valeur de l'as par dealer*************
        if dealer[-1] == "Ace":
                newchoice = 11
                acedealer.append(newchoice)
                print(acedealer)
                print(f"       => total: {newchoice}")

        time.sleep(1)

        for required in range(2):
            takecard(player)

        print(f"\nYour hand:\n{styled(player)}")

        #***choix valeur de l'as par player***
        if "Ace" in player:
            newchoice = 0
            while newchoice != 11 and newchoice != 1:
                newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
            aceplayer.append(newchoice)
            print(aceplayer)
        #***cas où pioche deux as***
            if player.count("Ace") == 2:
                newchoice = 0
                while newchoice != 11 and newchoice != 1:
                    newchoice = int(input("\n    ---> is second Ace worth 1 or 11?\n"))
                    aceplayer.append(newchoice)
                print(aceplayer)
        
        time.sleep(1)

        if total(player, aceplayer) == 21:
            print("       => BLACKJACK")      
        else:           
            print(f"       => total: {total(player, aceplayer)}")


        #****************************************
        #*************CHOIX D'ACTION*************
        #****************************************
        time.sleep(1)

        if total(player, aceplayer) < 21:
            
            action = input("\nWhat do you wish to do now?\n   Say 'hit' if you want another card.\n   Say 'stand' if you want to end your turn. The dealer hand will be revealed.\n   Say 'double' if you want to double your bet. You will take one last card.\n")
            #hit = input("\nSay 'hit' if you want another card.\nIf you don't the dealer hand will be revealed.\n")
                
            #while hit.lower() == "hit" and total(player, aceplayer) < 21:
            while action.lower() == "hit":
                card = random.choice(deck52)
                print("\nHere's your card:")
                time.sleep(1)
                takecard(player)
                print(styled(player))
                if player[-1] == "Ace":
                    newchoice = 0
                    while newchoice != 11 and newchoice != 1:
                        newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
                        aceplayer.append(newchoice)
                print(f"      => total: {total(player, aceplayer)}")
                time.sleep(1)
                #si blackjack ou supérieur à 21: pas de choix à faire
                if total(player, aceplayer) >= 21:
                    break
                else:
                    #hit = input("\nAgain? Say 'hit'\n")
                    action = input("\nWhat now? Say 'hit', 'double' or 'stand'.\n")
                    
            if action == "double":
                bet = bet*2
                card = random.choice(deck52)
                print("\nDOUBLE DOWN! Here's your card:")
                time.sleep(1)
                takecard(player)
                print(styled(player))
                if player[-1] == "Ace":
                    newchoice = 0
                    while newchoice != 11 and newchoice != 1:
                        newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
                        aceplayer.append(newchoice)
                print(f"      => total: {total(player, aceplayer)}")
                time.sleep(1)
            
            if action == "stand":
                time.sleep(1)
            
        #***************************************************
        #******REVEAL ET COMPLETE DE LA MAIN DU DEALER******
        #***************************************************
        time.sleep(2)

        print("Your turn ends. Revealing dealer's hand...\n")

        time.sleep(2)

        print(f"Dealer:\n{styled(dealer)}")

        if dealer[0] == "Ace":
                if (total(dealer, acedealer) + 11) <= 21:
                    newchoice = 11
                else:
                    newchoice = 1
                acedealer.append(newchoice)
                print(acedealer)

        if total(dealer, acedealer) < 17:
            time.sleep(1)
            print("\nCompleting dealer's hand until 17...")
            while total(dealer, acedealer) < 17:
                time.sleep(2)
                takecard(dealer)
                print(styled(dealer))
                print(f"       => total: {total(dealer, acedealer)}\n")
                if dealer[-1] == "Ace":
                    #newchoice = 0
                    if (total(dealer, acedealer) + 11) <= 21:
                        newchoice = 11
                    else:
                        newchoice = 1
                    acedealer.append(newchoice)
                time.sleep(2)
        elif total(dealer, acedealer) == 21:
            print("       => BLACKJACK\n")
        else:
            print(f"       => total: {total(dealer, acedealer)}\n")

                            
        #***************************************************
        #****************GAINS DU JOUEUR********************
        #****************(hors blackjack)*******************
        #***************************************************
        time.sleep(1)

        if total(player, aceplayer) > 21:
            print("Your bet is lost.")
        else:
            time.sleep(1)
            if total(dealer, acedealer) <= 21:
                if total(dealer, acedealer) > total(player, aceplayer):
                    print("Your bet is lost.\n")
                if total(dealer, acedealer) == total(player, aceplayer):
                    print("PUSH! Your bet is returned to you.\n")
                    wallet = wallet + bet
                if total(player, aceplayer) > total(dealer, acedealer) :
                    print("You win once your bet.\n")
                    wallet = wallet + bet*2
            #elif total(dealer, acedealer) > 21:
            else:
                print("You win once your bet.\n")
                wallet = wallet + bet*2
                    
        time.sleep(2)

        print(f"You now have {wallet}$.\n")

        time.sleep(2)

        replay = input("Do you still want to play? (y/n)\n")

    else:
        exit()

print("You're broke. Out!")

time.sleep(2)

exit()