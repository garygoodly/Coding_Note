import numpy as np
class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * n
        for i in range(n):
            prefix[i] = nums[i] + prefix[i - 1]
        
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
 
        ans = -np.inf
        for i in range(n - 1):  
            ans = max(ans, prefix[i] - suffix_min[i + 1])
        
        return ans