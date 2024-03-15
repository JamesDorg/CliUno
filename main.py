#main code here
import character
import card
import help

player = character.Character()
player2 = character.Character()
player3 = character.Character()
player4 = character.Character()

colorList = ["red", "green", "blue", "yellow", "black"]
numbList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
'''
comp = character.Character()
comp2 = character.Character()
comp3 = character.Character()
comp4 = character.Character()
'''
deck = character.Character()
discard = character.Character()

def menu():

    print("UNO\nWelcome to Uno!")
    player.name = input("What is your name? ")
    imp = ''
    
    while imp != "yes":
        num_players = input("How many players do you want? ")
        if num_players > 3:
            player2.name = input("What is the next person's name? ")
        elif num_players > 2:
            player3.name = input("What is the next person's name? ")
        elif num_players > 1:
            player4.name = input("What is the next person's name? ")


def create_deck():
    for i in range(4):
        for j in range(2):
            for k in range(10):
                deck.hand.append(card(numbList[k], colorList[i]))
    print(deck.hand)
create_deck()
    
        
        
    

    
    
menu()