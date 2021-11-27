from tkinter import Canvas

from cell import Cell


class Board:

    def __init__(self, root):
        self.world = root
        # self.board = []
        self.canvas = Canvas(self.world.window, width=self.world.size, height=self.world.size)
        self.canvas.pack()
        self.initialize_board()
        self.world.window.update()

    def initialize_board(self):
        self.canvas.delete("all")
        size = self.world.size
        rows = self.world.rows
        cols = self.world.cols

        # for i in range(rows):
        #     for j in range(cols):
        #         self.board.append((i, j))

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
        cell = Cell(self.world)
        row_h = int(self.world.size / self.world.rows)
        col_w = int(self.world.size / self.world.cols)
        x1 = cell.localisation[0] * row_h
        y1 = cell.localisation[1] * col_w
        x2 = x1 + row_h
        y2 = y1 + col_w
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=cell.color())
