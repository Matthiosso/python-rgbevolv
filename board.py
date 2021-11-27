from tkinter import Canvas

from cell import Cell


class Board:

    def __init__(self, root):
        self.world = root
        self.canvas = Canvas(self.world.window, width=self.world.size, height=self.world.size)
        self.canvas.pack()
        self.cells = []
        self.initialize_board()
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

    def merge_cells(self, cell1, cell2) -> Cell:
        return Cell(self.world, loc=cell1.loc, genome={
            'red': int((cell1.genome['red'] + cell2.genome['red']) / 2),
            'green': int((cell1.genome['green'] + cell2.genome['green']) / 2),
            'blue': int((cell1.genome['blue'] + cell2.genome['blue']) / 2)
        })

    def draw_cell(self):
        cell = Cell(self.world)

        existing_cells = [c for c in self.cells if c.loc[0] == cell.loc[0] and c.loc[1] == cell.loc[1]]
        if len(existing_cells) > 0:
            cell = self.merge_cells(cell1=cell, cell2=existing_cells[0])
        row_h = int(self.world.size / self.world.rows)
        col_w = int(self.world.size / self.world.cols)
        x1 = cell.loc[0] * row_h
        y1 = cell.loc[1] * col_w
        x2 = x1 + row_h
        y2 = y1 + col_w
        self.cells.append(cell)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=cell.color())
