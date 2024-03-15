#main code here
import character
import card
import help

player = character.Character()
player2 = character.Character()
player3 = character.Character()
player4 = character.Character()
'''
comp = character.Character()
comp2 = character.Character()
comp3 = character.Character()
comp4 = character.Character()
deck = character.Character()
discard = character.Character()
'''

def menu():

    print("UNO\nWelcome to Uno!")
    player.name = input("What is your name? ")
    imp = ''
    
    while imp != "yes":
        num_players = input("How many players do you want? ")
        if num_players > 3:
            player.name = input("What is the next person's name? ")
        elif num_players > 2:
            player.name = input("What is the next person's name? ")
        elif num_players > 1:
            player.name = input("What is the next person's name? ")


def create():
    pass
        
        
    

    
    
menu()