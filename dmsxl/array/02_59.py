class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        SpiralMatrix = [[0 for _ in range(n)] for _ in range(n)]
        X, Y = 0, -1
        k = 1
        for i in range(n-1, 0, -2):
            Y += 1
            for _ in range(0, i):
                SpiralMatrix[X][Y] = k
                Y += 1
                k += 1
            for _ in range(0, i):
                SpiralMatrix[X][Y] = k
                X += 1
                k += 1
            for _ in range(0, i):
                SpiralMatrix[X][Y] = k
                Y -= 1
                k += 1
            for _ in range(0, i):
                SpiralMatrix[X][Y] = k
                X -= 1
                k += 1
            X += 1
        if k == n**2:
            SpiralMatrix[X][Y + 1] = k

        return SpiralMatrix
if __name__ == "__main__":
    s = Solution()
    s.generateMatrix(2)
    s.generateMatrix(3)
    s.generateMatrix(4)
    s.generateMatrix(5)
    s.generateMatrix(1)