SUITS = ['hearts', 'spades', 'clubs', 'diamonds']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SYMBOLS = {
    "hearts": '♥',
    "spades": '♠',
    "diamonds": '♦',
    "clubs": '♣'
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return self.rank + SYMBOLS[self.suit] 


class Hand:
    def __init__(self, cards):
        self.cards = [Card(card["rank"], card["suit"]) for card in cards]

    def __repr__(self):
        return "-".join(map(str,self.cards))

    @property
    def value(self):
        value = 0
        aces = 0
        for c in self.cards:
            if c.rank in ['J', 'Q', 'K']:
                value += 10
            elif c.rank == 'A':
                value += 1
                aces += 1
            else:
                value += int(c.rank)
        while value < 12 and aces > 1:
            value += 10
            aces -= 1
        return value
