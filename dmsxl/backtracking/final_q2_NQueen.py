# 52

class Solution(object):
    def __init__(self):
        self.diag = set()
        self.inv_diag = set()
        self.visit = []
        self.ans = None

    def ans_appenda(self, curr):
        self.ans += 1

    def ans_append(self, curr):
        n = len(curr)
        arr = []
        for i in curr:
            arr.append("".join(["Q" if ii == i else "." for ii in range(n)]))
        self.ans.append(arr)


    def bta(self, n, curr):
        if len(curr) == n:
            self.ans_appenda(curr)
            return
        idx = len(curr)
        # print(curr)
        for i in range(n):
            if not self.visit[i]:
                if (idx + i not in self.diag
                        and n - idx + i not in self.inv_diag
                        and (idx == 0 or abs(curr[-1] - i) > 1)):
                    self.diag.add(idx + i)
                    self.inv_diag.add(n - idx + i)
                    self.visit[i] = True
                    self.bta(n, curr + [i])
                    self.diag.remove(idx + i)
                    self.inv_diag.remove(n - idx + i)
                    self.visit[i] = False

    def btb(self, n, curr):
        if len(curr) == n:
            self.ans_append(curr)
            return
        idx = len(curr)
        # print(curr)
        for i in range(n):
            if not self.visit[i]:
                if (idx + i not in self.diag
                        and n - idx + i not in self.inv_diag
                        and (idx == 0 or abs(curr[-1] - i) > 1)):
                    self.diag.add(idx + i)
                    self.inv_diag.add(n - idx + i)
                    self.visit[i] = True
                    self.btb(n, curr + [i])
                    self.diag.remove(idx + i)
                    self.inv_diag.remove(n - idx + i)
                    self.visit[i] = False

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = 0
        self.visit = [0] * n
        self.bta(n, [])
        return self.ans

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = []
        self.visit = [0] * n
        self.btb(n, [])
        return self.ans