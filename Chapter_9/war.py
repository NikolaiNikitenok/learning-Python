class Card():
    """ Создает колоду карт, каждая карта имеет свой номинал. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Трефы", "Бубны", "Червы", "Пики"]
    card = ''
    coloda = []
    nominal = 0
    
    def __init__(self):
        pass
    
    def card_create(self):
        for rank in self.RANKS:
            self.nominal = self.RANKS.index(rank) + 1
            for suit in self.SUITS:
                self.coloda_create(rank, suit)
                
    def coloda_create(self, rank, suit):
        self.card = str(rank) + '-' + str(suit) + " (" + str(self.nominal) + ")"
        self.coloda.append(self.card)
    

class Player():
    """ Создает игрока и раздает ему карту. """
    def __init__(self, name):
        import random
        self.hand = random.choice(Card.coloda)
        # self.nominal_hand = Card.nominal
        self.name = name
        print(self.name)
        print(self.hand)
        
        # self.nominalus = ''
        
        # for nom in self.hand:
        #     if nom.isdigit() and nom != self.hand[0]:
        #         self.nominalus += nom
        # print(self.nominalus)
        # print(Card.nominal)
        # print(self.nominal_hand)
        
        
        
class Game():
    """ Создание интерфейса игры. """
    def __init__(self, names):
        self.players = []
        self.nominalus = ''
        
        for name in names:
            player = Player(name)
            self.players.append(player)
            
        for nom in name.hand:
            if nom.isdigit() and nom != name.hand[0]:
                self.nominalus += nom
        print(self.nominalus)
            
            
Card().card_create()
print(Card().coloda)
names = ["Nikolai", "Nikita"]
game = Game(names)



