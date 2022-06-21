#!/usr/bin/python

import random

import getpass

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

deck52 = deck *4

#dealergame = {}
dealergame = []
#playergame = {}
playergame = []

def givevalue(card):
    """
    Returns how many gives a card

    Args:
        card: int ou str

    Return:
        integer: amount of points
    """    

    if type(card) == int:
        #value = card
        return card

    if type(card) == str and card != "Ace":
        #value = 10
        return 10

    if card == "Ace":
        acechoice = 0
        while acechoice != 11 and acechoice != 1:
            acechoice = int(input("Is Ace worth 1 or 11?\n"))
        #value = acechoice
        return acechoice


#****************************
#************JEU*************
#****************************

print(f"\nHello {getpass.getuser()}\n")

#remplacer pouic par autre chose
for pouic in range(2):
    card = random.choice(deck52)
    #dealergame["carte{0}".format(pouic)] = card
    dealergame.append(card)
    deck52.remove(card)

print(dealergame)
#pour accéder aux index il faut d'abord convertir en liste
#print(f"Dealer:\n< ? > < {list(dealergame.values())[1]} >")
print(f"Dealer:\n< ? > < {dealergame[1]} >")

for pouic in range(2):
    card = random.choice(deck52)
    #playergame["carte{0}".format(pouic)] = card
    playergame.append(card)
    deck52.remove(card)

print(playergame)

#print(f"Player:\n< {list(playergame.values())[0]} > < {list(playergame.values())[1]} >")
print(f"Player:\n< {playergame[0]} > < {playergame[1]} >")

#sum = givevalue(list(playergame.values())[0]) + givevalue(list(playergame.values())[1])
totalplayer = givevalue(playergame[0]) + givevalue(playergame[1])
totaldealer = givevalue(dealergame[0]) + givevalue(dealergame[1])

print(f"=> total: {totalplayer}")

#si blackjack, le joueur ne peut pas continuer et on révèle la carte du dealer
if totalplayer == 21:
    print("Blackjack")
    print("Revealing dealer's game...")
    print(f"Dealer:\n< {dealergame[0]} > < {dealergame[1]} >")
    if totaldealer == 21:
        print("Tie")
        #si égalité les joueurs récupèrent leurs mises 
    else:
        print("You win")
else:
    nextaction=input("Say 'hit' if you want to take another card. Otherwise, the game ends.")
    if nextaction == "hit":
        fdqsf
    else:


