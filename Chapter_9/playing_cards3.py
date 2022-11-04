# Карты 3.0
# Демонстрирует наследование в части переопределения методов

class Card():
    """ Одна игральная карта. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Трефы", "Бубны", "Червы", "Пики"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Unprintable_Card(Card):
    """ Карта, номинал и масть которой не могут быть выведены на экран. """
    def __str__(self):
        return "<нельзя напечатать>"


class Positionable_Card(Card):
    """ Карта, которую можно положить лицом или рубашкой вверх. """
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


# Основная часть
def main():
    card1 = Card("A", "Трефы")
    card2 = Unprintable_Card("A", "Буби")
    card3 = Positionable_Card("A", "Червы")

    print("Печатаю объект Card:")
    print(card1)
    print("\nПечатаю объект Unprintable_Card:")
    print(card2)
    print("\nПечатаю объект Positionable_Card:")
    print(card3)
    print("\nПереворачиваю объект Positionable_Card:")
    card3.flip()
    print("\nПечатаю объект Positionable_Card:")
    print(card3)

    input("Press Enter...")

if __name__ == "__main__":
    main()
