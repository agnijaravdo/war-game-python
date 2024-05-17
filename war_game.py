
class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suite}"
    
class Deck:
    def __init__(self):
        self.decks = []
        suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']


        

    
