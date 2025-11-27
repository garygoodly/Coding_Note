class Solution(object):
    def bt(self, ans, path, nums, start_idx):
        if start_idx == len(nums):
            return
        previous = None
        for i in range(start_idx, len(nums)):
            if previous != nums[i]:
                previous = nums[i]
                path.append(nums[i])
                ans.append(path[:])
                self.bt(ans, path, nums, i+1)
                path.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        