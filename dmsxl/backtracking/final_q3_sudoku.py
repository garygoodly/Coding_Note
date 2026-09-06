class Solution(object):

    def __init__(self):
        self.row_visit = [[False] * 10 for _ in range(9)]
        self.col_visit = [[False] * 10 for _ in range(9)]
        self.block_visit = [[False] * 10 for _ in range(9)]

    @staticmethod
    def get_block(row, col):
        return 3 * (row // 3) + col // 3

    def bt(self, idx, board):

        if idx == 81:
            return True

        row = idx // 9
        col = idx % 9

        # Already filled
        if board[row][col] != '.':
            return self.bt(idx + 1, board)

        block = self.get_block(row, col)

        for num in range(1, 10):

            if (self.row_visit[row][num]
                    or self.col_visit[col][num]
                    or self.block_visit[block][num]):
                continue

            # choose
            board[row][col] = str(num)

            self.row_visit[row][num] = True
            self.col_visit[col][num] = True
            self.block_visit[block][num] = True

            # recurse
            if self.bt(idx + 1, board):
                return True

            # undo
            board[row][col] = '.'

            self.row_visit[row][num] = False
            self.col_visit[col][num] = False
            self.block_visit[block][num] = False

        return False

    def solveSudoku(self, board):

        for row in range(9):
            for col in range(9):

                if board[row][col] != '.':
                    num = int(board[row][col])
                    block = self.get_block(row, col)

                    self.row_visit[row][num] = True
                    self.col_visit[col][num] = True
                    self.block_visit[block][num] = True

        self.bt(0, board)