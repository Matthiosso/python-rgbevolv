import uuid
import random


class Cell:
    def __init__(self, root, loc=None, genome=None):
        self.id = str(uuid.UUID)

        if genome:
            self.genome = genome
        else:
            self.genome = {
                'red': random.randrange(0, 255),
                'green': random.randrange(0, 255),
                'blue': random.randrange(0, 255)
            }

        if loc:
            self.loc = loc
        else:
            self.loc = (random.randrange(0, root.rows), random.randrange(0, root.cols))

    def color(self):
        return '#%02x%02x%02x' % (self.genome['red'], self.genome['green'], self.genome['blue'])

    def __str__(self) -> str:
        return 'Cell {id=%s;genome=%s;loc=(%i, %i)}' % (self.id, self.genome, self.loc[0], self.loc[1])

