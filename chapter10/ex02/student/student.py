# File: studentlisttest.py
from student import Student
import random

def main():
    # 1. Öğrenci nesnelerini oluştur
    students = [
        Student("Alice"),
        Student("Bob"),
        Student("Charlie"),
        Student("David"),
        Student("Eve")
    ]

    # 2. Her öğrencinin skorlarını sıfırla (veya isteğe bağlı doldur)
    for student in students:
        student.scores = [0] * 10

    # 3. Önce sırasız listeyi yazdır
    print("Unsorted list of students:")
    for s in students:
        print(s)
    
    # 4. Listeyi karıştır
    random.shuffle(students)

    # 5. Karışık listeyi yazdır
    print("\nShuffled list of students:")
    for s in students:
        print(s)
    
    # 6. Listeyi isimlerine göre sırala
    students.sort()  # __lt__ metodu student.py içinde tanımlı olmalı

    # 7. Sıralanmış listeyi yazdır
    print("\nSorted list of students:")
    for s in students:
        print(s)

if __name__ == "__main__":
    main()
