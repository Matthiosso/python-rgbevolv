import uuid
import random


class Cell:
    def __init__(self, root):
        self.id = str(uuid.UUID)
        self.genome = {
            'red': random.randrange(0, 255),
            'green': random.randrange(0, 255),
            'blue': random.randrange(0, 255)
        }
        self.move_nb = 100
        self.localisation = (random.randrange(0, root.rows), random.randrange(0, root.cols))
        self.parent_1 = None
        self.parent_2 = None

    def color(self):
        return '#%02x%02x%02x' % (self.genome['red'], self.genome['green'], self.genome['blue'])
