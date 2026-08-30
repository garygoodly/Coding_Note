from collections import defaultdict

class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_table = defaultdict(int)
        for i in nums:
            freq_table[i] += 1
        
        freq_of_freq_table = defaultdict(int)
        for key, val in freq_table.items:
            if freq_of_freq_table[val] == 0:
                freq_of_freq_table[val] = 1
            else:
                freq_of_freq_table[val] = -1
            
        for i in nums:
            if freq_of_freq_table[freq_table[i]] == 1:
                return i
        return -1