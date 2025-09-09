from collections import defaultdict

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h1 = defaultdict(bool)
        h2 = defaultdict(bool)

        for i in nums1:
            h1[i] = True

        for i in nums2:
            h2[i] = True

        ans = []
        for k, v in h1.items():
            if h2[k] == True:
                ans.append(k)

        return ans
    

############################################################
    
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h1 = set(nums1)
        h2 = set(nums2)

        ans = []
        for k in h1:
            if k in h2:
                ans.append(k)

        return ans