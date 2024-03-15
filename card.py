class Card():
    def __init__(self, symbol, color):
        self.symbol=symbol
        self.color=color
    def checkplayable(self, old):
        if self.symbol==old.symbol or self.color==old.color:
            return(True)
        else:
            return(False)