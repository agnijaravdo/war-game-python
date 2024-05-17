
class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suite}"

    def __repr__(self) -> str:
        return f"{self.value} of {self.suite}"
    
class Deck:
    def __init__(self):
        self.decks = []
        self.suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    
    def create_deck(self):
        for suite in self.suites:
            for value in self.values:
                card = Card(suite, value)
                self.decks.append(card)
        return self.decks

deck = Deck()
print(deck.create_deck())
        

    
