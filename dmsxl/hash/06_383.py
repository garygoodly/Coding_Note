from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictM = defaultdict(int)

        for c in magazine:
            dictM[c] += 1
        
        for c in ransomNote:
            if dictM[c] == 0:
                return False
            
            dictM[c] -= 1
        return True