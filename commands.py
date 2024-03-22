import character
import card
import commands
import main

def help():
    print("Help menu:")
    print("rules: Displays all the rules.")
    print("start: Starts the game. Get ready!")

def rules():
    print("Rulebook:")
    print("You can choose how many people play before the game starts. \n If you choose to play solo though, a computer bot will play you instead.")
    print("At the start of the game, everyone will be given seven cards.")
    print("You then will take turns playing the cards. \n You can only place a card down if the card you choose is either the same number or color of the card on the deck. \n The first person to run out wins.")
    
def menu():

    print("UNO\nWelcome to Uno!")
    main.player.name = input("What is your name? ")
    imp = ''
    
    while imp != "yes":
        num_players = int(input("How many players do you want? "))
        if num_players > 3:
            main.player4.name = input("What is the next person's name? ")
        else:
            main.player4.name = "None"

        if num_players > 2:
            main.player3.name = input("What is the next person's name? ")
        else:
            main.player3.name = "None"

        if num_players > 1:
            main.player2.name = input("What is the next person's name? ")
        else:
            main.player2.name = "None"

        
        print("Players: " + main.player.name + ", " + main.player2.name + ", ", main.player3.name + ", " + main.player4.name)
        imp = input("(yes/no) Is this correct? ")
