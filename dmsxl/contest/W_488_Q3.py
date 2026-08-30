class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        l, r = 0, 0
        max_q = deque()
        min_q = deque()
        for r in range(n):
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()
            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            max_q.append(r)
            min_q.append(r)
            
            while (nums[max_q[0]] - nums[min_q[0]]) * (r - l + 1) > k:
                if min_q[0] == l:
                    min_q.popleft()
                if max_q[0] == l:
                    max_q.popleft()
                l += 1
            ans += (r - l + 1)
        return ans