from tkinter import Canvas

import numpy as np

from cell import Cell


class Board:

    def __init__(self, root):
        self.world = root
        self.canvas = Canvas(self.world.window, width=self.world.size, height=self.world.size)
        self.canvas.pack()
        self.cell = Cell(0)
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

    def draw_cell(self):
        row_h = int(self.world.size / self.world.rows)
        col_w = int(self.world.size / self.world.cols)
        x1 = self.cell.loc[0] * row_h
        y1 = self.cell.loc[1] * col_w
        x2 = x1 + row_h
        y2 = y1 + col_w
        self.initialize_board()
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.cell.color)

    def is_move_forbidden(self, cell):
        return cell.loc[0] < 0 or cell.loc[0] > self.world.rows-1 or cell.loc[1] < 0 or cell.loc[1] > self.world.cols-1

    def move_cell(self):
        self.cell.move()
        if self.is_move_forbidden(self.cell):
            self.cell.step_back()
            if len(self.cells) > 0:
                if self.cell.move_nb > self.cells[-1].move_nb:
                    self.cells.append(self.cell)
                    print('New cell nb %i (moves: %i) using hist ' % (len(self.cells), self.cell.move_nb),
                          self.cell.hist)
            else:
                self.cells.append(self.cell)
                # print('New cell nb %i using hist ' % len(self.cells), self.cell.hist)

            self.cell = Cell(len(self.cells), hist=self.cell.hist)
        self.draw_cell()
