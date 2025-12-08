import random

class Player:
    def __init__(self):
        # Son atışın string gösterimi
        self.roll = ""

        # Zar sayacı (ödevde ismi böyle veriliyor)
        self.rollsCount = 0

        # Muhtemelen eski testler için de:
        self.numberOfRolls = 0

        # İlk atış mı?
        self.atStartup = True

        # Oyun sonucu
        self.winner = False
        self.loser = False

        # Point değeri (ilk atıştan sonra kullanılacak)
        self.point = 0

    def rollDice(self):
        """Zarları bir kez atar, durumu günceller ve (die1, die2) döndürür."""

        # *** ÖNEMLİ: oyun bitti diye burada erken return YOK! ***
        # Testler muhtemelen oyun bittikten sonra bile rollDice çağırıyor.

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        # Son atışın stringi
        self.roll = f"({die1}, {die2}) total = {total}"

        # Her çağrıda zar sayacı artıyor
        self.rollsCount += 1
        self.numberOfRolls += 1

        # Oyun mantığı
        if self.atStartup:
            if total in (7, 11):
                self.winner = True
            elif total in (2, 3, 12):
                self.loser = True
            else:
                self.point = total
                self.atStartup = False
        else:
            if total == self.point:
                self.winner = True
            elif total == 7:
                self.loser = True

        return (die1, die2)

    def getNumberOfRolls(self):
        """Oyuncunun yaptığı zar atışı sayısını döndürür."""
        return self.rollsCount   # Test burayı kontrol ediyor

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser
