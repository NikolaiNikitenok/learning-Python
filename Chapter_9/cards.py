# Модуль cards
# Набор базовых классов для карточной игры

class cards():
    """ Одна игральная карта. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Трефы", "Бубны", "Червы", "Пики"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
