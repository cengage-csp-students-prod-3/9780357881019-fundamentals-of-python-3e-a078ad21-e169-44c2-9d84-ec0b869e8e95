import random

def shuffleString(theString):
    chars = list(theString)      # listeye çevir
    random.shuffle(chars)        # shuffle geri değer döndürmez
    print("".join(chars))        # karıştırılmış listeyi join et

shuffleString("Apples are red")
