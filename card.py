class Card():
    def __init__(self):
        self.symbol="na"
        self.color="na"
    def checkplayable(self, old):
        if self.symbol==old.symbol or self.color==old.color:
            return(True)
        else:
            return(False)