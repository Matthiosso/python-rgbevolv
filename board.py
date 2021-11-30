from tkinter import Canvas

from cell import Cell
from cellbranch import CellBranch
from enum import Enum, auto


class MoveResult(Enum):
    FORBIDDEN_MOVEMENT = auto()
    ALLOWED_MOVEMENT = auto()
    SUCESS_MOVEMENT = auto()


class Board:

    def __init__(self, root):
        self.world = root
        self.canvas = Canvas(self.world.window, width=self.world.size, height=self.world.size)
        self.canvas.pack()
        self.cells_pool = [CellBranch(name) for name in ['toto', 'titi', 'tata', 'trotro']]
        self.board = root.map
        self.draw_cells()
        self.world.window.update()

    def initialize_board(self):
        self.canvas.delete("all")
        size = self.world.size
        rows = self.world.rows
        cols = self.world.cols

        for i in range(cols):
            self.canvas.create_line(
                i * size / cols, 0, i * size / cols, size,
            )

        for i in range(rows):
            self.canvas.create_line(
                0, i * size / rows, size, i * size / rows,
            )

        for i in range(rows):
            for j in range(cols):
                if self.board[i][j] == 1:
                    self.draw_cell(Cell(loc=(i, j)), '#696969')
                elif self.board[i][j] == 2:
                    self.draw_cell(Cell(loc=(i, j)), '#FF0000')

    def draw_cells(self):
        self.initialize_board()
        for cell_b in self.cells_pool:
            self.draw_cell(cell_b.current_cell, cell_b.color)

    def draw_cell(self, cell: Cell, color):
        row_h = int(self.world.size / self.world.rows)
        col_w = int(self.world.size / self.world.cols)
        y1 = cell.loc[0] * row_h
        x1 = cell.loc[1] * col_w
        x2 = x1 + col_w
        y2 = y1 + row_h
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def check_move(self, cell: Cell):
        if cell.loc[0] < 0 or cell.loc[0] > self.world.rows - 1 or cell.loc[1] < 0 or \
                cell.loc[1] > self.world.cols - 1 or self.board[cell.loc[0]][cell.loc[1]] == 1:
            return MoveResult.FORBIDDEN_MOVEMENT
        elif self.board[cell.loc[0]][cell.loc[1]] > 1:
            return MoveResult.SUCESS_MOVEMENT
        else:
            return MoveResult.ALLOWED_MOVEMENT

    def move_cell(self):
        for cell_branch in self.cells_pool:
            cell = cell_branch.current_cell
            cell.move()
            movement = self.check_move(cell)
            if movement == MoveResult.FORBIDDEN_MOVEMENT:
                cell.step_back()
                cell_branch.new()
            elif movement == MoveResult.SUCESS_MOVEMENT:
                print(f'Well Done Cell {cell_branch.name}')
                self.world.run = False
                self.world.over = True

        self.draw_cells()
