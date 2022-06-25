#!/usr/bin/python

import random

import getpass

import time

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

deck52 = deck *4

dealerhand = []

playerhand = []

wallet = 100

acechoice = []

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

        
#test de def dans une def
def total(hand):
    """
    Returns total number of points in a player's hand

    Args:
        hand(list): player's or dealer's hand

    Return:
        integer: total amount of points
    """
    totalace = 0
    total = 0
    if hand.count("Ace") >= 1:
        for ace in acechoice:
            totalace = totalace + ace
    for card in hand:
        total = total + givevalue(card)
    return totalace + total
  

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


def drawcard(hand):
    """
    Draws a random card from the deck and adds it to the list "playerhand"

    Args:
        player: defines which hand will be updated (player or dealer's)
    """
    card = random.choice(deck52)
    hand.append(card)
    deck52.remove(card)

#***à finir***
def getback(bet):
    """
    Refunds your bet by adding back bet value to the variable "wallet"

    Args:
        bet: amount of the bet in dollars
    """
    wallet = wallet + bet


#****************************
#************JEU*************
#****************************

print(f"\nWelcome {getpass.getuser()}\n")

time.sleep(2)

#***à faire***
bet = int(input("How much do yo wish to bet?\n"))

wallet = wallet - bet

#************************************
#**********MAINS DE DEPART***********
#************************************
print("\nLet's look at the hands...\n")

time.sleep(2)

#voir pour faire fonction drawcard avec 2 args où 2ème serait nombre d'itérations
for required in range(2):
    drawcard(dealerhand)

print(f"Dealer:\n< ? >  < {dealerhand[1]} >\n")

time.sleep(1)

for required in range(2):
    drawcard(playerhand)

print(f"Your hand:\n{styled(playerhand)}")

if "Ace" in playerhand:
    newchoice = 0
    while newchoice != 11 and newchoice != 1:
        newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
        acechoice.append(newchoice)
        print(acechoice)
#***QUID SI DEUX AS???***
    if playerhand.count("Ace") == 2:
        newchoice = 0
        while newchoice != 11 and newchoice != 1:
            newchoice = int(input("\n    ---> is second Ace worth 1 or 11?\n"))
            acechoice.append(newchoice)
        print(acechoice)
 
time.sleep(1)

if total(playerhand) == 21:
    print("     BLACKJACK!")      
else:           
    print(f"       => total: {total(playerhand)}")


#****************************************
#*************CHOIX D'ACTION*************
#****************************************
time.sleep(1)

if total(playerhand) < 21:
    
    action = input("\nWhat do you wish to do now?\nSay 'hit' if you want another card.\nSay 'stand' if you want the hand to end. The dealer hand will be revealed.\nSay 'double' if you want to double your bet. You will draw one last card.\n")
    #hit = input("\nSay 'hit' if you want another card.\nIf you don't the dealer hand will be revealed.\n")
        
    #while hit.lower() == "hit" and total(playerhand) < 21:
    while action.lower() == "hit":
        card = random.choice(deck52)
        print("\nHere's your card:")
        time.sleep(1)
        drawcard(playerhand)
        print(styled(playerhand))
        if playerhand[-1] == "Ace":
            newchoice = 0
            while newchoice != 11 and newchoice != 1:
                newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
                acechoice.append(newchoice)
        print(f"      => total: {total(playerhand)}")
        time.sleep(1)
        #si blackjack ou supérieur à 21: pas de choix à faire
        if total(playerhand) >= 21:
            break
        else:
            #hit = input("\nAgain? Say 'hit'\n")
            action = input("\nWhat now? Say 'hit', 'double' or 'stand'.\n")
            
    if action == "double":
        bet = bet*2
        card = random.choice(deck52)
        print("\nDOUBLE DOWN! Here's your card:")
        time.sleep(1)
        drawcard(playerhand)
        print(styled(playerhand))
        if playerhand[-1] == "Ace":
            newchoice = 0
            while newchoice != 11 and newchoice != 1:
                newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
                acechoice.append(newchoice)
        print(f"      => total: {total(playerhand)}")
        time.sleep(1)
    
    if action == "stand":
        time.sleep(1)
        print("You will take no more card")
    
#***************************************************
#******REVEAL ET COMPLETE DE LA MAIN DU DEALER******
#***************************************************
time.sleep(2)

print("\nThe hand ends. Revealing dealer's hand...\n")

time.sleep(1)

print(f"Dealer:\n{styled(dealerhand)}\n")

if total(dealerhand) < 17:
    time.sleep(1)
    print("Completing dealer's hand until 17...")
    time.sleep(2)
while total(dealerhand) < 17:
    time.sleep(1)
    drawcard(dealerhand)
    print(styled(dealerhand))
print(f"       => total: {total(dealerhand)}\n")
# if total(dealerhand) > 21:
#     print("Dealer loses")

#***************************************************
#****************GAINS DU JOUEUR********************
#*****************hors blackjack********************
#***************************************************

#***perdu***
if total(playerhand) > 21:
    print("Your bet is lost")        

#***soft blackjack et tie blackjack***
if total(playerhand) == 21 and total(dealerhand) != 21:
    time.sleep(1)
    print("You win once your bet.\n")
    wallet = wallet + 2*bet

if total(dealerhand) == total(playerhand) == 21:
    time.sleep(1)
    print("TIE! Your bet is returned to you.\n")
    wallet = wallet + bet
    
#***moins de 21***
if total(playerhand) < 21:
    time.sleep(1)
    if total(dealerhand) <= 21:
        if total(dealerhand) > total(playerhand):
            print("Dealer wins. Your bet is lost.\n")
        elif total(dealerhand) == total(playerhand):
            print("PUSH! Your bet is returned to you.\n")
        else:
            print("Your hand's better than the dealer's. You win once your bet.\n")
            wallet = wallet + bet*2

time.sleep(1)             
print(f"You have {wallet}$ left.")
