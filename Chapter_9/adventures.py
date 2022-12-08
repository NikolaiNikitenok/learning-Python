class Hero():
    """ Создание игрока, который может перемещаться по точкам, ближайшим к нему. """
    def __init__(self, name, position=0):
        self.name = name
        self.position = position


class Map():
    """ Создание карты с координатами точек, в которые можно перемещаться. """
    def __init__(self):
        self.positions = []
        
    def __str__(self):
        rep = f"There are such points on the map now: \n"
        for place in self.positions:
            plus = f"Place's name: {place.name};\tPlace's position: {place.position}\n"
            rep += plus
        return rep
        
    def add_place(self, name, position):
        """ Добавление места на карту. """
        place = Place(name, position)
        self.positions.append(place)


class Place():
    """ Создание места с координатами, в которое можно переместиться. """
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def __str__(self):
        rep = f"Place's name: {self.name};\nPlace's position: {self.position}"
        return rep

class Game():
    pass