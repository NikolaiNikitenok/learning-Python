import random

class Lottery():
    def __init__(self):
        self.items = [123, 348, 736, 965, 234, 546, 777, 830, 390, 523, "a", "z", "w", "h", "j"]
        
    def generate_ticket(self):
        self.number = random.choices(self.items, k=4)
        return self.number
    
    def generate_phrase(self):
        self.win_number = ""
        for num in self.number:
            self.win_number += str(num)
            
        self.phrase = f"Билет, содержащий эту комбинацию: {self.win_number}, выиграл!!!"
        return self.phrase
    

class Me():
    def __init__(self):
        self.lottery = Lottery()
        self.my_ticket = self.lottery.generate_ticket()
        
    def how_many_times_to_win(self):
        winner = self.lottery.generate_ticket()
        times = 1
        while winner != self.my_ticket:
            print(winner)
            winner = self.lottery.generate_ticket()
            times += 1
            
        print(f"Тебе понадобилось {times} попыток, чтобы выиграть в лотерее!")
        
            


lot1 = Lottery()
print(lot1.generate_ticket())

me = Me()
me.how_many_times_to_win()
