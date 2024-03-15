import card

class Character():
    def __init__(self):
        self.name = None
        self.save_point = 0
        self.hand = []

    def draw_card(self):
        self.hand.append(card.Card())

    def play_card(self, pt):
        curr_card = self.deck[pt]
        self.hand.pop(pt)
        return curr_card
    
    def end_turn(self):
        self.save_point += 1
    
    def display(self):
        

        
        
    