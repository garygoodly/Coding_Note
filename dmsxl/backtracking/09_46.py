class Solution(object):
    def bt(self, ans, path, used, nums):
        if len(path) == len(nums):
            ans.append(path[:])
            return
        
        for idx, val in enumerate(nums):
            if used[idx] == False:
                used[idx] = True
                path.append(val)
                self.bt(ans, path, used, nums)
                used[idx] = False
                path.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        used = [False] * len(nums)
        self.bt(ans, [], used, nums)
        return ans