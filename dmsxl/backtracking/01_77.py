class Solution(object):
    def backtracking(self, ans, path, n, k):
        if len(path) == k:
            ans.append(path)
            return
        
        if len(path) == 0:
            for i in range(1, n - k + 2):
                self.backtracking(ans, [i], n, k)
        else:
            for i in range(path[-1] + 1, n - k + len(path) + 2):
                self.backtracking(ans, path + [i], n, k)
        return
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.backtracking(ans, [], n, k)
        return ans
    

class Solution(object):
    def backtracking(self, ans, path, n, k, startIdx):
        if len(path) == k:
            ans.append(path[:])
            return
        
        for i in range(startIdx, n + 1):
            path.append(i)
            self.backtracking(ans, path, n, k, i + 1)
            path.pop()
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.backtracking(ans, [], n, k, 1)
        return ans
    
class Solution(object):
    def backtracking(self, ans, path, n, k, startIdx):
        if len(path) == k:
            ans.append(path[:])
            return
        
        for i in range(startIdx, n - k + len(path) + 2):
            path.append(i)
            self.backtracking(ans, path, n, k, i + 1)
            path.pop()
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.backtracking(ans, [], n, k, 1)
        return ans