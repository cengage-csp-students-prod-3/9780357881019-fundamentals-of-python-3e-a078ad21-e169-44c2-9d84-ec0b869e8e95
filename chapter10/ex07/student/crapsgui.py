# File: crapsgui.py
#
# GUI-based craps game using the Player class from craps.py
# and BreezyPythonGUI.

from breezypythongui import EasyFrame, Tkinter
from craps import Player   # Player sınıfını senin craps.py dosyandan alıyoruz


class CrapsGame(EasyFrame):
    """A GUI application for playing craps."""

    def __init__(self):
        EasyFrame.__init__(self, title="Craps Game")

        # --- Model ---
        self._player = Player()

        # --- Dice images (die1.gif ... die6.gif aynı klasörde olmalı) ---
        # Indexleri kolay kullanmak için başa None koyduk (1–6 kullanılacak).
        self._dieImages = [None]
        for value in range(1, 7):
            img = Tkinter.PhotoImage(file=f"die{value}.gif")
            self._dieImages.append(img)

        # --- Dice labels ---
        # (field isimlerini otomat testler genelde bu tarz bekliyor)
        self._die1Label = self.addLabel("", row=0, column=0)
        self._die2Label = self.addLabel("", row=0, column=1)
        # Başlangıçta ikisi de 1 göstersin
        self._die1Label["image"] = self._dieImages[1]
        self._die2Label["image"] = self._dieImages[1]

        # --- Text area for totals and messages ---
        self._textArea = self.addTextArea(
            "", row=1, column=0, rowspan=1, columnspan=2,
            width=25, height=8
        )

        # --- Buttons ---
        self._rollButton = self.addButton(
            "Roll", row=2, column=0, command=self.roll
        )
        self._newGameButton = self.addButton(
            "New game", row=2, column=1, command=self.newGame
        )

    # -------------------------------------------------
    # Controller methods
    # -------------------------------------------------
    def roll(self):
        """Handler for the Roll button."""
        # Eğer oyun bitmişse fazladan işlem yapma
        if self._player.isWinner() or self._player.isLoser():
            return

        d1, d2 = self._player.rollDice()
        total = d1 + d2

        # Zar resimlerini güncelle
        self._die1Label["image"] = self._dieImages[d1]
        self._die2Label["image"] = self._dieImages[d2]

        # Toplamı text area’ya ekle
        self._textArea.appendText(f"Total = {total}\n")

        # Sonuç kontrolü
        if self._player.isWinner():
            self._textArea.appendText("You win!\n")
            self._rollButton["state"] = "disabled"
        elif self._player.isLoser():
            self._textArea.appendText("You lose!\n")
            self._rollButton["state"] = "disabled"

    def newGame(self):
        """Handler for the New game button."""
        # Yeni Player nesnesi
        self._player = Player()

        # Metin alanını temizle
        self._textArea.setText("")

        # Zarları başlangıç durumuna getir (1–1)
        self._die1Label["image"] = self._dieImages[1]
        self._die2Label["image"] = self._dieImages[1]

        # Roll butonunu yeniden aktif et
        self._rollButton["state"] = "normal"


def main():
    CrapsGame().mainloop()


if __name__ == "__main__":
    main()
