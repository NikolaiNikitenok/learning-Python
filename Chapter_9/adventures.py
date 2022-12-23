class Hero():
    """ Создание игрока, который может перемещаться по точкам, ближайшим к нему. """
    def __init__(self, name, position=0):
        self.name = name
        self.position = position


class Map():
    """ Создание карты c координатами точек, в которые можно перемещаться. """
    def __init__(self):
        self.positions = []
        
    def __str__(self):
        rep = f"There are such points on the map now: \n"
        for place in self.positions:
            plus = f"Place's name: {place.name};\tPlace's position: {place.position}\n"
            rep += plus
        return rep
        
    def posit(self):
        posit_spisok = []
        for place in self.positions:
            pass
            
    def add_place(self, name, position):
        """ Добавление места на карту. """
        place = Place(name, position)
        self.positions.append(place)


class Place():
    """ Создание места c координатами, в которое можно переместиться. """
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def __str__(self):
        rep = f"Place's name: {self.name};\nPlace's position: {self.position}"
        return rep

class Game():
    def __init__(self, name):
        self.player = Hero(name)
        
    def generate_map(self):
        map = Map()
        map.add_place("Place1", 1)
        map.add_place("Place2", 3)
        map.add_place("Place3", 2)
        map.add_place("Place4", 7)
        print(map)
        map.posit()
        # print(map.positions)
        
    def blizko(self):
        pos = []
        
    
    def play(self):
        self.generate_map()
    
def main():
    game = Game("Nikolai")
    game.play()
    
if __name__ == "__main__":
    main()
    