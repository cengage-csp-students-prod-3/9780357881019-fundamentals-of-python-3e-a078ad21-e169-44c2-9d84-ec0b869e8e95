import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts."""

    def __init__(self, fileName=None):
        """Creates a new dictionary to hold the accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except Exception:
                    fileObj.close()
                    break

    def __str__(self):
        """Returns the string representation of the bank with accounts sorted by name."""
        # accounts.values() listesini al, SavingsAccount sınıfındaki __lt__ metoduna göre sırala
        sorted_accounts = sorted(self.accounts.values())
        return "\n".join(map(str, sorted_accounts))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and returns it, or None if the account does not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank, or returns None if the account does not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys."""
        return sorted(self.accounts.keys())

    def save(self, fileName=None):
        """Saves pickled accounts to a file."""
        if fileName is not None:
            self.fileName = fileName
        elif self.fileName is None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()


# Functions for testing
def createBank(numAccounts=1):
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testBank(number=0):
    bank = Bank()
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1),
                                str(1000 + i),
                                100.00))
    return bank

def main(number=10, fileName=None):
    bank = testBank(9)
    print(bank)

if __name__ == "__main__":
    main()
