# Игра "Война"
# Все игроки тянут по одной карте, а выигрывает тот, у кого номинал карты оказывается наибольшим.

import cards, games


class War_Card(cards.Card):
    """ Создадим 1 карту """
    @property
    def value(self):
        v = War_Card.RANKS.index(self.rank) + 1


# Создание колоды
class War_Deck(cards.Deck):
    """ Колода. """
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))


class War_Hand(cards.Hand):
    """ Карты на руках у 1 игрока. """
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    
    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
        return t


class War_Player(War_Hand):
    def lose(self):
        print(self.name, "проиграл,")

    def win(self):
        print(self.name, "выиграл!")

    def push(self):
        print(self.name, "сыграли в ничью.")
        
        
class War_Game():
    def __init__(self, names):
        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)
            
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
        
    def play(self):
        sp = []  # Список значений на руках у всех игроков
        self.deck.deal(self.players, per_hand=1)
        for player in self.players:
            sp.append(player.total)
        print(player)
            
def main():
    print("\t\tДобро пожаловать за игровой стол!\n")
    names = []
    number = games.ask_number("Сколько всего игроков? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name)
        print()
    game = War_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nХотите сыграть еще раз? ")
        
main()
input("\n\nPress Enter...")
    