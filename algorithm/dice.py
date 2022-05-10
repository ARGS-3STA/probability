import random


class Dice:
    def __init__(self, sides: int = 2) -> None:
        self.sides = sides

    def toss(self) -> int:
        return random.randint(1, self.sides)

    def die(self) -> int:
        return random.randint(1, 6)

    def coin(self) -> int:
        return random.randint(1, 2)
