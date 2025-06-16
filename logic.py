import random

class BingoLogic:
    def __init__(self, max_number = 99):
        self.max_number = max_number
        self.remaining = list(range(1, max_number +1))
        random.shuffle(self.remaining)
        self.drawn = []

    def draw(self):
        if not self.remaining:
            return None
        num = self.remaining.pop()
        self.drawn.append(num)
        return num

    def get_drawn(self):
        return list(self.drawn)
