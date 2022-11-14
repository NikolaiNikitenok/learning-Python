# Игра "Война"
# Все игроки тянут по одной карте, а выигрывает тот, у кого номинал карты оказывается наибольшим.

import cards, games


class War_Card(cards.Card):
    """ Создадим 1 карту """
    @property
    def value(self):
        v = War_Card.RANKS.index(self.rank) + 1
        
        return v


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
        # print(t)
        return t
    
    # def all_total(self):
    #     tot = 


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
        
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            sp.append(player)
        return sp
        
    def play(self):
        self.deck.deal(self.players, per_hand=1)
        for player in self.players:
            print(player)
            
    def winner(self, names):
        self.all_total = []
        
        for name in names:
            player_total = War_Player(name).total
            self.all_total.append(player_total)
            
            print(self.all_total)

        # spisok_all_points = []
        # for hand in self.
        
        
            
def main():
    print("\t\tДобро пожаловать за игровой стол!\n")
    names = []
    number = games.ask_number("Сколько всего игроков? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name)
        # print(names)
    game = War_Game(names)
    game.play()
    game.winner(names)
    print(War_Player(names).total)
        
main()
input("\n\nPress Enter...")
    