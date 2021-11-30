from tkinter import Tk

from board import Board

WINDOW_SIZE = 600
DELAY = 100

WORLD = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2]
]

# WORLD = [
#     [0, 1, 1],
#     [0, 0, 0],
#     [1, 1, 0],
#     [0, 0, 0],
#     [2, 1, 1],
# ]

WORLD_SIZE_HEIGHT = len(WORLD)
WORLD_SIZE_WIDTH = len(WORLD[0])


class World:
    def __init__(self):
        self.window = Tk()
        self.window.title('RGB Evolv')
        self.window.configure(bg='black')
        self.size = WINDOW_SIZE
        self.rows = WORLD_SIZE_HEIGHT
        self.cols = WORLD_SIZE_WIDTH
        self.map = WORLD

        self.board = Board(self)
        self.window.bind("<Key>", self.key_input)
        self.run = False
        self.over = False

    @staticmethod
    def check_if_key_valid(key):
        valid_keys = ['space', 'Escape']
        if key in valid_keys:
            return True
        else:
            return False

    def key_input(self, event):
        key_pressed = event.keysym
        # Check if the pressed key is a valid key
        if self.check_if_key_valid(key_pressed):
            if key_pressed == 'space' and not self.over:
                self.run = not self.run
                print('Running : ', self.run)
            elif key_pressed == 'Escape':
                self.run = False
                self.over = True
                print('Bye bye')
                self.window.destroy()

    def mainloop(self):
        while True:
            self.window.update()
            if self.run:
                self.window.update_idletasks()
                self.window.after(DELAY, self.board.move_cell())
