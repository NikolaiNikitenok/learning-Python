# Блек-Джек
# От й до 7 игроков против дилера

import cards, games


class BJ_Card(cards.Card):
    """ Карта для игры в Блек-Джек. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(cards.Deck):
    """ Колода для игры в "Блек-джек". """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """ 'Рука': набор карт "Блек-Джека" у одного игрока. """
    def __init__(self, name):  # Добавляем в конструктор родителя
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # Если у одной из карт value = None, то и все свойство равно None
        for card in self.cards:
            if not card.value:
                return None

        # Суммируем очки, считая каждый туз за 1 очко
        t = 0
        for card in self.cards:
            t += card.value

        # Определяем, есть ли туз на руках у игрока
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # Если на руках есть туз и сумма очков не превышает 11, будем считать туз за 11 очков
        if contains_ace and t <= 11:
            # Прибавить нужно только 10, потому что единица уже вошла в общую сумму
            t += 10
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """ Игрок в Блек-Джек. """
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", будете еще брать карты? (y/n): ")
        return response == "y"

    def bust(self):
        print(self.name, "перебрал.")
        self.lose()

    def lose(self):
        print(self.name, "проиграл,")

    def win(self):
        print(self.name, "выиграл!")

    def push(self):
        print(self.name, "сыграл с компьютером в ничью.")

class BJ_Dealer(BJ_Hand):
    """ Дилер в игре "Блек-джек". """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрал.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ Игра в Блек-джек. """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # Сдача всем по 2 карты
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  # Пеервая из карт, сданных дилеру, переворачивается рубашкой вверх.
        for player in self.players:
            print(player)
        print(self.dealer)
        # Сдача дополнительных карт игрокам
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()  # Первая карта дилера раскрывается
        if not self.still_playing:
            # Все игроки перебрали, покажем только "руку" дилера
            print(self.dealer)
        else:
            # Сдача дополнительных карт дилеру
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                # Выигрывают все, кто еще остался в игре
                for player in self.still_playing:
                    player.win()
            else:
                # Сравниваем суммы очков у дилера и у игроков, оставшихся в игре
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        # Удаление всех карт
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\t\tДобро пожаловать за игровой стол Блек-джека!\n")
    names = []
    number = games.ask_number("Сколько всего игроков? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nХотите сыграть еще раз? ")

main()
input("\n\nPress Enter...")
