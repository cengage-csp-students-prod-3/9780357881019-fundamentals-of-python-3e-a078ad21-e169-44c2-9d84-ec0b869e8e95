# Write your code here# File: cardsgui.py
#
# GUI program to deal and view cards from a deck.

from breezypythongui import EasyFrame, Tkinter
from cards import Deck, Card


class CardsDemo(EasyFrame):
    """GUI application to display cards from a deck."""

    def __init__(self):
        EasyFrame.__init__(self, title="Cards Demo")

        # Model: deck of cards
        self._deck = Deck()

        # Resim önbelleği
        self._cardImages = {}  # key: (rank, suit) -> PhotoImage

        # Kart arka yüzü resmi (DECK/b.gif)
        self._backImage = Tkinter.PhotoImage(file="DECK/b.gif")

        # Kart resmi için label
        # (3 sütun kaplasın ki butonlarla hizalansın)
        self._imageLabel = self.addLabel(
            "", row=0, column=0, columnspan=3, sticky="N"
        )
        self._imageLabel["image"] = self._backImage

        # Kart açıklaması için label (örn. "Queen of Hearts")
        self._textLabel = self.addLabel(
            "", row=1, column=0, columnspan=3, sticky="N"
        )

        # Butonlar
        self._dealButton = self.addButton(
            "Deal", row=2, column=0, command=self.deal
        )
        self._shuffleButton = self.addButton(
            "Shuffle", row=2, column=1, command=self.shuffle
        )
        self._newDeckButton = self.addButton(
            "New deck", row=2, column=2, command=self.newDeck
        )

    # ---------- Helper methods ----------

    def cardToImage(self, card):
        """Returns the PhotoImage associated with this Card.
           If card.faceup is False, returns the back image."""
        if not card.faceup:
            return self._backImage

        key = (card.rank, card.suit)
        if key in self._cardImages:
            return self._cardImages[key]

        # Suit harfleri: s, d, h, c
        suitLetters = {
            "Spades": "s",
            "Diamonds": "d",
            "Hearts": "h",
            "Clubs": "c"
        }
        suitLetter = suitLetters[card.suit]
        filename = f"DECK/{card.rank}{suitLetter}.gif"

        img = Tkinter.PhotoImage(file=filename)
        self._cardImages[key] = img
        return img

    # ---------- Button callbacks ----------

    def deal(self):
        """Deals the top card and displays it."""
        card = self._deck.deal()
        if card is None:
            # Deste bitti, sadece bilgi yaz
            self._textLabel["text"] = "No more cards"
            self._imageLabel["image"] = self._backImage
            return

        # Kartı yüzü yukarı çevir
        if not card.faceup:
            card.turn()

        # Resmi ve yazıyı güncelle
        img = self.cardToImage(card)
        self._imageLabel["image"] = img
        self._textLabel["text"] = str(card)

    def shuffle(self):
        """Shuffles the deck and resets the view to back image."""
        self._deck.shuffle()
        self._imageLabel["image"] = self._backImage
        self._textLabel["text"] = ""

    def newDeck(self):
        """Creates a new deck and resets the display."""
        self._deck = Deck()
        self._imageLabel["image"] = self._backImage
        self._textLabel["text"] = ""


def main():
    CardsDemo().mainloop()


if __name__ == "__main__":
    main()
