class Card:
    def __init__(self,rank, suit):
        self.rank=rank
        self.suit=suit

    def __repr__(self):
        return "Card('{}','{}')".format(self.rank, self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit


from random import shuffle
class Deck():
    # ranks and suits means  the Deck class variables
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']

    def __init__(self):
        self.deck= []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append(Card(rank, suit))



    def __eq__(self, other):
        return self.deck == other.deck

    def __len__(self):
        return len(self.deck)

    def dealCard(self):
        return self.deck.pop()

    def shuffle(self):
        shuffle(self.deck)

deck=Deck()
deck.shuffle()
card=Card('A','\u2660')
print(deck.dealCard())
print(card.getRank())




