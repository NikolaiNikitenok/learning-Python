class Card():
    """ Создает колоду карт, каждая карта имеет свой номинал. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Трефы", "Бубны", "Червы", "Пики"]
    card = ''
    coloda = []
    
    def __init__(self):
        pass
    
    def coloda_create(self, rank, suit):
        self.card = str(rank) + '-' + str(suit)
        self.coloda.append(self.card)
        
    
    def card_create(self):
        for rank in self.RANKS:
            for suit in self.SUITS:
                self.coloda_create(rank, suit)
                
                
        
Card().card_create()
print(Card().coloda)
