class Solution(object):
    def bt(self, ans, path, nums, start_idx):
        if start_idx == len(nums):
            return
        
        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            ans.append(path[:])
            self.bt(ans, path, nums, i+1)
            path.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        self.bt(ans, [], nums, 0)
        return ans