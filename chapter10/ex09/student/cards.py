"""
File: cards.py

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = tuple(range(1, 14))
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        # Yeni: kartın yüzü yukarı mı?
        self.faceup = False

    # Yeni: turn metodu
    def turn(self):
        """Turns the card over (face up <-> face down)."""
        self.faceup = not self.faceup
        
    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        return str(rank) + " of " + self.suit


class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        """Shuffles the cards, all turned face down again."""
        random.shuffle(self.cards)
        # Bütün kartları tekrar yüzü kapalı yapalım
        for card in self.cards:
            card.faceup = False

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self.cards.pop(0)

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(self.cards)

    def __str__(self): 
        """Returns the string representation of a deck."""
        result = ""
        for c in self.cards:
            result = result + str(c) + '\n'
        return result
