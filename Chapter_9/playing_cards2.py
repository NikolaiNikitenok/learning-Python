# Карты 2.0
# Демонстрирует расширение класса через наследование

class Card(object):
    """ Одна игральная карта. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Трефы", "Бубны", "Червы", "Пики"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + " " +self.suit
        return rep


class Hand(object):
    """ 'Рука': набор карт на руках у одного игрока. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ Колода игральных карт. """
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать, карты закончились!")


# Основная часть

def main():
    deck1 = Deck()
    print("Создана новая колода!")
    print("Вот эта колода: ")
    print(deck1)

    deck1.populate()
    print("\nВ колоде появились карты!")
    print("Вот как она выглядит теперь:")
    print(deck1)



if __name__ == "__main__":
    main()
