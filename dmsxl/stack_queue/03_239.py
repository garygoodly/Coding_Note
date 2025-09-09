from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums

        queue = deque()     # [1,3,-1,-3,5,3,6,7]
        ans = []
        for i in range(k - 1):
            while (len(queue) and queue[-1][1] <= nums[i]):
                queue.pop()
            queue.append((i, nums[i]))

        for i in range(k - 1, len(nums)):
            while(queue[0][0] + k <= i):
                queue.popleft()
            while (len(queue) and queue[-1][1] <= nums[i]):
                queue.pop()
            queue.append((i, nums[i]))
            ans.append(queue[0][1])
        return ans