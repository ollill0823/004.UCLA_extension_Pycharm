class Card:
    def __init__(self,rank, suit):
        self.rank=rank
        self.suit=suit

    def __repr__(self):
        print('({}, {})'.format(self.rank, self.suit))

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

print( Card('3','\u2660') == Card('3','\u2660') )
print( Card('3','\u2660') == eval(repr(Card('3','\u2660') )) )