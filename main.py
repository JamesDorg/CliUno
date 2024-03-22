#main code here
import character
import card


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

cur_player = None

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
    create_deck()
    imp = ''
    
    
    while imp != "yes":
        '''
        num_players = int(input("How many players do you want? "))
        if num_players > 3:
            player4.name = input("What is the next person's name? ")
        else:
            player4.name = "None"

        if num_players > 2:
            player3.name = input("What is the next person's name? ")
        else:
            player3.name = "None"

        if num_players > 1:
            player2.name = input("What is the next person's name? ")
        else:
            player2.name = "None"

        '''
        '''
        player.name = input("What is your name? ")
        player2.name = input("What is the other person's name? ")

        print("Players: " + player.name + ", " + player2.name)
        '''
        imp = input("(yes/no) Is this correct? ")
        

    start_game()

def create_deck():
    for i in range(4):
        for j in range(2):
            for k in range(10):
                h = deck.hand
                c = card.Card(numbList[k], colorList[i])
                h.append(c)
    #print(deck.hand[0].symbol)
                
def start_game():
    
    for i in range(7):
        player.draw_card(deck.play_card(-1))
        player2.draw_card(deck.play_card(-1))
    
    deck.name = "1"
    discard.draw_card(deck.play_card(-1))
    play_turn()
    

def rotate_turn():
    pass

def play_turn():

    print(deck.name)

    
    if deck.name == '1':
        cur_player = player
        deck.name = '2'
    else:
        cur_player = player2
        deck.name = '1'
    
    cur_player = player
    cur_player.display()
    print(discard.hand[-1].symbol, discard.hand[-1].color)

    imp = int(input("Which card would you like to play"))
    try:
        discard.draw_card(cur_player.play_card(imp-1))
    except:
        print("Not a valid option please draw one.")
        cur_player.draw_card(deck.play_card(-1))

    if len(cur_player.hand) == 0:
        print("Yay you won,", cur_player.name)
    
    play_turn()
   

def cli(IN):
    pass

    
menu()