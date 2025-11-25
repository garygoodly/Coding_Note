class Solution(object):
    def is_valid(self, s, start, end):
        if end != start and s[start] == '0':
            return False
        num = int(s[start : end + 1])
        return 0 <= num <= 255
    
    def bt(self, s, ans, path, start_idx):
        if len(path) == 4:
            if start_idx == len(s):
                ans.append(".".join(path))
            return

        for i in range(start_idx, min(start_idx + 3, len(s))):
            if self.is_valid(s, start_idx, i):
                path.append(s[start_idx : i+1])
                self.bt(s, ans, path, i + 1)
                path.pop()

        return

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.bt(s, ans, [], 0)
        return ans