class Solution(object):
    def backtracking(self, ans, n, k):
        if len(ans[0]) == k:
            return
        for i in range(1, n - k - ans[0]):
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        