class Die():
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        import random
        number = random.randint(1, self.sides)
        print(f"Выпало число: {number}")
        
        
cube = Die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()

cube2 = Die(10)
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()
cube2.roll_die()

cube3 = Die(20)
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
cube3.roll_die()
    