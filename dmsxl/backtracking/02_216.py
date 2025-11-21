class Solution(object):
    def bt(self, ans, path, n, k, start, sum):
        if len(path) == k:
            if sum == n:
                ans.append(path[:])
            return
        


        # for i in range(start, 10):
        for i in range(start, 9 - k + 2 + len(path)):
            path.append(i)
            sum += i
            self.bt(ans, path, n, k, i + 1, sum)
            path.pop()
            sum -= i


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.bt(ans, [], n, k, 1, 0)
        return ans