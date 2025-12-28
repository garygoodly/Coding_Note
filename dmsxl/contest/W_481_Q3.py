from collections import defaultdict
class Solution(object):
    def minSwaps(self, nums, forbidden):
        """
        :type nums: List[int]
        :type forbidden: List[int]
        :rtype: int
        """
        same = 0
        n = len(nums)
        table = defaultdict(int)
        same_table = defaultdict(int)
        for i in range(n):
            if nums[i] == forbidden[i]:
                same += 1
                same_table[nums[i]] += 1
            table[nums[i]] += 1
            table[forbidden[i]] += 1
        
        for k, v in table.items():
            if v > n:
                return -1
        

        max_cost = 0 
        for k, v in same_table.items():
            max_cost = max(v, max_cost)

        residue = same - max_cost
        swap_time = same - residue * 2

        return (same + 1) // 2 if swap_time <= 1 else swap_time