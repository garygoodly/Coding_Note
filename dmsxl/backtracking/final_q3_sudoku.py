class Solution(object):
    def __init__(self):
        self.board = None
        self.board_fix = [[0] * 9 for _ in range(9)]
        self.row_visit = [[0] * 10 for _ in range(9)]
        self.col_visit = [[0] * 10 for _ in range(9)]
        self.block_visit = [[0] * 10 for _ in range(9)]

    @staticmethod
    def map(row, col):
        return 3 * (row // 3) + col // 3

    def bt(self, row, col):



    def solveSudoku(self, board):
        self.board = board
        self.board_fix = [[1 if self.board[i][j] != '.' else 0 for j in range(9)] for i in range(9)]

        for row in range(9):
            for col in range(9):
                if self.board[row][col] != '.':
                    tmp = int(self.board[row][col])
                    self.row_visit[row][tmp] = 1
                    self.col_visit[col][tmp] = 1
                    self.block_visit[self.map(row, col)][tmp] = 1
        #
        # print(self.row_visit)
        # print(self.col_visit)
        # print(self.block_visit)