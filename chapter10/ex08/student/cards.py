"""
File: cards.py

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit, rank, and faceup attribute."""

    RANKS = tuple(range(1, 14))
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit

        # Task 1: faceup instance variable (default False)
        self.faceup = False

    # Task 2: turn method
    def turn(self):
        """Turns the card over by negating the faceup flag."""
        self.faceup = not self.faceup

    def __str__(self):
        """Returns the string representation of a card,
           now including faceup status."""
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

        # Add faceup status to printed output
        return f"{rank} of {self.suit} {self.faceup}"


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
        """Shuffles the cards."""
        random.shuffle(self.cards)

        # When shuffled, turn all cards face up (as in sample output)
        for card in self.cards:
            card.faceup = True

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


def main():
    """A simple test."""
    deck = Deck()
    print("A new deck, cards face down:")
    while len(deck) > 0:
        print(deck.deal())

    deck = Deck()
    deck.shuffle()
    print("A deck shuffled once, cards face up:")
    while len(deck) > 0:
        print(deck.deal())

if __name__ == "__main__":
    main()
