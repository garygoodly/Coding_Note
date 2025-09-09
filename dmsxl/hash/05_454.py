from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        DicSum12 = defaultdict(int)

        for i in nums1:
            for j in nums2:
                DicSum12[i + j] += 1

        return sum(DicSum12[-i - j] for i in nums3 for j in nums4)