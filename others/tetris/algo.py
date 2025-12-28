import time
import numpy as np
import random
import pygame

GRID_SIZE = 30
BOARD_WIDTH = 12
BOARD_HEIGHT = 24
WINDOW_WIDTH = BOARD_WIDTH * GRID_SIZE
WINDOW_HEIGHT = BOARD_HEIGHT * GRID_SIZE

class Tetromino:
    Tetromino_size_enum = {
        0: 'I',
        1: 'O',
        2: 'L',
        3: 'T',
        4: 'FL',
        5: 'N',
        6: 'FN'
    }

    Tetromino_color_enum = {
        'I':  (0, 255, 255),   # Ao
        'O':  (255, 255, 0),   # Yellow
        'L':  (255, 165, 0),   # Orange
        'FL': (0, 0, 255),     # Blue
        'T':  (160, 32, 240),  # Purple
        'N':  (0, 255, 0),     # Green
        'FN': (255, 0, 0)      # Red
    }

    Tetromino_block = {
        'I': [[0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0]],

        'O': [[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]],
    
        'L': [[0, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 1, 1],
              [0, 0, 0, 0]],
              
        'T': [[0, 0, 0, 0],
              [0, 0, 1, 0],
              [0, 1, 1, 1],
              [0, 0, 0, 0]],

        'FL':[[0, 0, 0, 0],
              [0, 0, 1, 0],
              [1, 1, 1, 0],
              [0, 0, 0, 0]],

        'FN':[[0, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 0]],

        'N': [[0, 0, 1, 0],
              [0, 1, 1, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 0]],
    }

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.shape = self.Tetromino_size_enum[type]
        self.arr = self.Tetromino_block[self.shape]
    
    def rotate(self):   # counter clockwise
        transposed = [[self.arr[j][i] for j in range(4)] for i in range(4)]
        self.arr = transposed[::-1]

    def rotate_c(self):   # clockwise
        flipped = self.arr[::-1]
        self.arr = [[flipped[j][i] for j in range(4)] for i in range(4)]

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

class Board:
    def __init__(self):
        self.grid = np.zeros(shape=(24, 12))
        self.grid[:, 0] = 1
        self.grid[:, 11] = 1
    
    def is_valid(self, tetro):
        for i in range(4):
            for j in range(4):
                if tetro.arr[i][j] + self.grid[tetro.y + i][tetro.x + j] > 1:
                    return False
        return True

    def update(self, tetro):
        for i in range(4):
            for j in range(4):
                if tetro.arr[i][j] == 1:
                    self.grid[tetro.y + i][tetro.x + j] = 1
    
    def clear_row(self):
        for i in range(24):
            if self.grid[i][:] == [1] * 12:
                self.grid[1 : i+1] = self.grid[ : i]
    


class Game:
    def __init__(self):
        self.board = Board()
        self.tetro = None

    def newTetro(self):
        self.tetro = Tetromino(4, 0, random.randint(0, 6))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))






        pygame.display.update()

    pygame.quit()