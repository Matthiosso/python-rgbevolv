import random


class Cell:
    def __init__(self, id=0, hist=None, loc=None):
        self.id = id
        self.move_nb = 0
        self.loc = loc if loc else (0, 0)
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
            while new_loc == self.loc or (self.move_nb > 1 and len(self.hist) > 1
                                          and new_loc == self.hist[self.move_nb-2]):
                move_on_x = bool(random.getrandbits(1))
                move = random.choice([1, 0, -1])
                if move_on_x:
                    new_loc = (self.loc[0] + move, self.loc[1])
                else:
                    new_loc = (self.loc[0], self.loc[1] + move)

            self.loc = new_loc
            self.move_nb += 1
            self.hist.append(self.loc)

    def step_back(self):
        if len(self.hist) > 0:
            self.hist.pop()
            self.move_nb -= 1
