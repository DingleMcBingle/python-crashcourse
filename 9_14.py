from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        x = randint(1, self.sides)
        print("You rolled a " + str(x) + ".")

ten_sides = Die(10)
twenty_sides = Die(20)

ten_sides.roll_dice()
twenty_sides.roll_dice()
