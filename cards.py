class Card:
    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    ranks = ['narf', 'Ace', '2', '3', '4', '5', '6', '7',
    '8' ,'9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank 


    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

