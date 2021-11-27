from tkinter import Tk

from board import Board

WINDOW_SIZE = 600
WORLD_SIZE_HEIGHT = 6
WORLD_SIZE_WIDTH = 8
DELAY = 100


class World:
    def __init__(self):
        self.window = Tk()
        self.window.title('RGB Evolv')
        self.window.configure(bg='black')
        self.size = WINDOW_SIZE
        self.rows = WORLD_SIZE_HEIGHT
        self.cols = WORLD_SIZE_WIDTH

        self.board = Board(self)
        self.window.bind("<Key>", self.key_input)
        self.run = False

    def check_if_key_valid(self, key):
        valid_keys = ['space', 'esc']
        if key in valid_keys:
            return True
        else:
            return False

    def key_input(self, event):
        key_pressed = event.keysym
        # Check if the pressed key is a valid key
        if self.check_if_key_valid(key_pressed):
            if key_pressed == 'space':
                self.run = not self.run
                print('Running : ', self.run)

    def mainloop(self):
        # self.window.mainloop()
        while True:
            self.window.update()
            if self.run:
                self.window.update_idletasks()
                self.window.after(DELAY, self.board.draw_cell())
