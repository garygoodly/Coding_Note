class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        if nums[0] == nums[-1] == 0:
            ans.append([0] * 3)

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    right -= 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1
                else:
                    right -= 1
        return ans