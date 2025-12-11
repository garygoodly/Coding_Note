import time
import numpy as np

class Tetromino:
    Tetromino_enum = {
        0: 'I',
        1: 'O',
        2: 'L',
        3: 'T',
        4: 'FL',
        5: 'N',
        6: 'FN'
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
        self.shape = self.Tetromino_enum[type]
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

if __name__ == '__main__':
    b = Board()
    
