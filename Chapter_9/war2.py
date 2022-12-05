class Card():
    """ Одна игральная карта. """
    
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Трефы", "Бубны", "Червы", "Пики"]
    
    def __init__(self, rank, suit, nominal):
        self.rank = rank
        self.suit = suit
        self.nominal = nominal

    @property
    def nominalus(self):
        v = self.nominal
        return v
        
    def __str__(self):
        rep = str(self.rank) + '-' + str(self.suit) + ' (' + str(self.nominal) + ')'
        return rep
        
class Hand():
    def __init__(self, name):
        self.cards = []
        self.name = name
        
    def __str__(self):
        rep = f'{self.name}: \t'
        for card in self.cards:
            rep += str(card) + '\t'
        return rep
        
    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.nominal
        return t
        
    def add(self, card):
        self.cards.append(card)
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
        
class Deck(Hand):
    
    def __init__(self):
        self.cards = []
        
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                nominal = Card.RANKS.index(rank) + 1
                self.add(Card(rank, suit, nominal)) # Вызов метода находящегося внутри себя
                
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
                    print("Распаковал новую колоду карт! Тщательно перемешал новую колоду!")
                    self.populate()


class Player(Hand):
    def lose(self):
        print(self.name, "проиграл,")

    def win(self):
        print(self.name, "выиграл!")

    def push(self):
        print(self.name, "сыграл в ничью.")


class Game():
    def __init__(self, names):
        self.players = []
        for name in names:
            player = Player(name)
            self.players.append(player)
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()
        
    def play(self):
        totals = []
        self.deck.deal(self.players)
        for player in self.players:
            print(player)
            totals.append(player.total)
        
        ind = totals.index(max(totals))
        winner = self.players[ind]
        winner.win()
        # print(f"Победил: {winner}!")
            
            
def main():
    names = ['Nikolai', 'Nikita', 'Gleb', 'Pipiska']
    game = Game(names)
    game.play()
    
main()