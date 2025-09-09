from collections import deque

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        letterStack = deque()
        for c in s:
            if len(letterStack) != 0:
                if letterStack[-1] == c:
                    letterStack.pop()
            letterStack.append(c)
        ans = "".join(letterStack)
        return ans