from collections import defaultdict
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        DictS = defaultdict(int)
        DictT = defaultdict(int)

        if (len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            DictS[s[i]] += 1
            DictT[t[i]] += 1

        return DictS == DictT
    
        return Counter(s) == Counter(t)