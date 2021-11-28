from tkinter import Canvas

import numpy as np

from cell import Cell


class Board:

    def __init__(self, root):
        self.world = root
        self.canvas = Canvas(self.world.window, width=self.world.size, height=self.world.size)
        self.canvas.pack()
        self.cell = Cell(self.world, 0)
        self.cells = []
        # self.board = np.zeros((self.world.rows, self.world.cols))
        self.draw_cell()
        self.world.window.update()

    def initialize_board(self):
        self.canvas.delete("all")
        size = self.world.size
        rows = self.world.rows
        cols = self.world.cols

        for i in range(rows):
            self.canvas.create_line(
                i * size / rows, 0, i * size / rows, size,
            )

        for i in range(cols):
            self.canvas.create_line(
                0, i * size / cols, size, i * size / cols,
            )

    def reset(self):
        self.canvas.delete("all")

    # def merge_cells(self, cell1, cell2) -> Cell:
    #     return Cell(self.world, loc=cell1.loc, genome={
    #         'red': int((cell1.genome['red'] + cell2.genome['red']) / 2),
    #         'green': int((cell1.genome['green'] + cell2.genome['green']) / 2),
    #         'blue': int((cell1.genome['blue'] + cell2.genome['blue']) / 2)
    #     })

    def draw_cell(self):
        row_h = int(self.world.size / self.world.rows)
        col_w = int(self.world.size / self.world.cols)
        x1 = self.cell.loc[0] * row_h
        y1 = self.cell.loc[1] * col_w
        x2 = x1 + row_h
        y2 = y1 + col_w
        self.initialize_board()
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.cell.color)

    def move_cell(self):
        if not self.cell.move():
            if len(self.cells) > 0:
                if self.cell.move_nb > self.cells[-1].move_nb:
                    self.cells.append(self.cell)
                    print('New cell nb %i (moves: %i) using hist ' % (len(self.cells), self.cell.move_nb),
                          self.cell.hist)
            else:
                self.cells.append(self.cell)
                # print('New cell nb %i using hist ' % len(self.cells), self.cell.hist)

            self.cell = Cell(self.world, len(self.cells), hist=self.cell.hist)
        self.draw_cell()
