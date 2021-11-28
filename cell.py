import random


class Cell:
    def __init__(self, root, id, hist=None):
        self.id = id
        self.move_nb = 0
        self.rows = root.rows
        self.cols = root.cols

        self.color = '#000000'
        self.loc = (0, 0)
        self.hist = hist if hist else []

    def __str__(self) -> str:
        return 'Cell {id=%i;hist=%s;loc=(%i, %i)}' % (self.id, self.hist, self.loc[0], self.loc[1])

    def move(self) -> bool:

        if self.move_nb < len(self.hist):
            self.loc = self.hist[self.move_nb]
            self.move_nb += 1
            return True

        new_loc = self.loc
        # Here we make it not to stay at the same place nor to repeat the same last movement.
        while new_loc == self.loc or (self.move_nb > 0 and len(self.hist) > 0 and new_loc == self.hist[self.move_nb-1]):
            new_loc = (self.loc[0] + random.choice([1, 0, -1]), self.loc[1] + random.choice([1, 0, -1]))

        self.loc = new_loc

        if self.loc[0] < 0 or self.loc[0] > self.rows-1 or self.loc[1] < 0 or self.loc[1] > self.cols-1:
            return False

        self.move_nb += 1
        self.hist.append(self.loc)
        return True
