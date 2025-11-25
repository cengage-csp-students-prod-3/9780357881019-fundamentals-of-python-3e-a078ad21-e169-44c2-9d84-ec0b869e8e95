# testmyrange.py

def myRange(start, stop=None, step=None):
    # -------------------------
    # 1. PARAMETRELERİ AYARLA
    # -------------------------
    if stop is None:  # sadece 1 argüman verilmişse
        stop = start
        start = 0

    if step is None:  # step belirtilmemişse
        step = 1

    # step = 0 olamaz → boş liste
    if step == 0:
        return []

    result = []

    # ---------------------------------------
    # 2. YÖN KONTROLÜ (infinite loop önleme)
    # ---------------------------------------
    # start < stop → artan şekilde gidilmeli, step > 0 olmalı
    if start < stop and step < 0:
        return []

    # start > stop → azalan şekilde gidilmeli, step < 0 olmalı
    if start > stop and step > 0:
        return []

    # -------------------------
    # 3. LİSTEYİ OLUŞTUR
    # -------------------------

    # Artan yön
    if step > 0:
        current = start
        while current < stop:
            result.append(current)
            current += step

    # Azalan yön
    else:
        current = start
        while current > stop:
            result.append(current)
            current += step  # step negatif

    return result


def main():
    print(myRange(10))           # [0..9]
    print(myRange(1, 10))        # [1..9]
    print(myRange(1, 10, 2))     # [1, 3, 5, 7, 9]
    print(myRange(10, 1, -1))    # [10..2]
    print(myRange(5, 5))         # []
    print(myRange(5, 1, 1))      # step yanlış → []
    print(myRange(1, 5, -1))     # step yanlış → []
    print(myRange(5, 1, 0))      # step 0 → []

if __name__ == "__main__":
    main()
