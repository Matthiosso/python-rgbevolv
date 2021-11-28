import numpy as np

from cell import Cell


class CellBranch:

    def __init__(self, name):
        self.name = name
        self.current_cell = Cell()
        self.dead_ones = []
        self.color = '#' + ''.join(['%02x' % s for s in list(np.random.choice(range(256), size=3))])

    def new(self):
        self.dead_ones.append(self.current_cell)
        self.current_cell = Cell(id=len(self.dead_ones), hist=self.current_cell.hist)
        return self.current_cell
