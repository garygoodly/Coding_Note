class Solution(object):
    def is_palindrome(self, s, start, end):
        i = start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def bt(self, ans, path, s, start_idx):
        if start_idx == len(s):
            ans.append(path[::])
            return
        
        for i in range(start_idx, len(s)):
            if self.is_palindrome(s, start_idx, i):
                path.append(s[start_idx : i+1])
                self.bt(ans, path, s, i+1)
                path.pop()
            
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        self.bt(ans, [], s, 0)
        return ans