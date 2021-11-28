import random


class Cell:
    def __init__(self, id, hist=None):
        self.id = id
        self.move_nb = 0
        self.color = '#000000'
        self.loc = (0, 0)
        self.hist = hist if hist else []

    def __str__(self) -> str:
        return 'Cell {id=%i;hist=%s;loc=(%i, %i)}' % (self.id, self.hist, self.loc[0], self.loc[1])

    def move(self):
        if self.move_nb < len(self.hist):
            self.loc = self.hist[self.move_nb]
            self.move_nb += 1
        else:
            new_loc = self.loc
            # Here we make it not to stay at the same place nor to repeat the same last movement.
            while new_loc == self.loc or (self.move_nb > 0 and len(self.hist) > 0 and new_loc == self.hist[self.move_nb-1]):
                new_loc = (self.loc[0] + random.choice([1, 0, -1]), self.loc[1] + random.choice([1, 0, -1]))

            self.loc = new_loc
            self.move_nb += 1
            self.hist.append(self.loc)

    def step_back(self):
        if len(self.hist) > 0:
            self.hist.pop()
            self.move_nb -= 1