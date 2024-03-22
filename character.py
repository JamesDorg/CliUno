import card

class Character():
    def __init__(self):
        self.name = None
        self.save_point = 0
        self.hand = []

    def draw_card(self, x):
        self.hand.append(x)

    def play_card(self, pt):
        curr_card = self.hand[pt]
        self.hand.pop(pt)
        return curr_card
    
    def end_turn(self):
        self.save_point += 1
    
    def display(self):
        print(self.name)
        print("Your cards: ")
        for i in self.hand:
            print(i.symbol, i.color, end = ", ")

    def play(self):
        pass

        
        
    