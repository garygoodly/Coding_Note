from collections import Counter

class Solution(object):
# ver 1: 
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        ans = []
        freq_table = [[0 for _ in range(26)] for _ in range(n)]
        for idx, w in enumerate(words):
            for c in w:
                freq_table[idx][ord(c) - ord('a')] += 1
        
        for i in range(26):
            tmp = min(w[i] for w in freq_table)
            ans += [chr(i + ord('a'))] * tmp
        
        return ans

# ver 2:
    def commonChars(self, words):
        FreqTable = Counter(words[0])
        for w in words:
            FreqTable &= Counter(w)

        ans = []
        for k, v in FreqTable.items():
            ans += [k] * v

        return ans