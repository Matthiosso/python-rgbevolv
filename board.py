from tkinter import Canvas

from cell import Cell
from cellbranch import CellBranch


class Board:

    def __init__(self, root):
        self.world = root
        self.canvas = Canvas(self.world.window, width=self.world.size, height=self.world.size)
        self.canvas.pack()
        self.cells_pool = [CellBranch(name) for name in ['toto', 'titi', 'tata', 'trotro']]
        self.board = [[None for _ in range(self.world.cols)] for _ in range(self.world.rows)]
        self.draw_cells()
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

    def draw_cells(self):
        self.initialize_board()
        for cell_b in self.cells_pool:
            self.draw_cell(cell_b.current_cell, cell_b.color)

    def draw_cell(self, cell: Cell, color):
        row_h = int(self.world.size / self.world.rows)
        col_w = int(self.world.size / self.world.cols)
        x1 = cell.loc[0] * row_h
        y1 = cell.loc[1] * col_w
        x2 = x1 + row_h
        y2 = y1 + col_w
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def is_move_forbidden(self, cell: Cell):
        return cell.loc[0] < 0 or cell.loc[0] > self.world.rows - 1 or cell.loc[1] < 0 or cell.loc[
            1] > self.world.cols - 1

    def move_cell(self):
        for cell_branch in self.cells_pool:
            cell = cell_branch.current_cell
            cell.move()
            if self.is_move_forbidden(cell):
                cell.step_back()
                must_save = not cell_branch.dead_ones or cell.move_nb > cell_branch.dead_ones[-1].move_nb

                cell = cell_branch.new()
                if must_save:
                    print('New cell from branch %s nb %i (moves: %i) using hist ' %
                          (cell_branch.name, cell.id, cell.move_nb), cell.hist)

        self.draw_cells()
