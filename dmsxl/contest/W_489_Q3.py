class Solution(object):
    
    def f(self, l, r, n, s):
        next_flag = False
        skip_flag = False
        skip_left, skip_right = False, False
        ans = 0
        while (l >= 0 and r < n and next_flag == False):
            if s[l] == s[r]:
                ans = max(ans, r - l + 1)
                print(s[l:r+1], ans, l, r)
                l -= 1
                r += 1
            else:
                skip_flag = True
                curr_l, curr_r = l, r
                l -= 1
                while (l >= 0 and r < n):
                    if s[l] == s[r]:
                        skip_left = True
                        ans = max(ans, r - l + 1)
                        print(s[l:r+1], ans, l, r)
                        l -= 1
                        r += 1
                    else:
                        l, r = curr_l, curr_r
                        next_flag = True
                        break
                r += 1
                while (l >= 0 and r < n):
                    if s[l] == s[r]:
                        skip_right = True
                        ans = max(ans, r - l + 1)
                        print(s[l:r+1], ans, l, r)
                        l -= 1
                        r += 1
                    else:
                        next_flag = True
                        l, r = curr_l, curr_r
                        break
        if skip_left == False and skip_right == False:
            l += 1
            r -= 1
            if (r - l + 1 < n):
                ans = max(ans, r - l + 2)
                print(s[l:r+1], ans, l, r)
        return ans


    
    def almostPalindromic(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        n = len(s)
        ans = 0

        for i, c in enumerate(s):
            l = r = i
            ans = max(ans, self.f(l, r, n, s))
            if (i < n - 1):
                l, r = i, i + 1
                ans = max(ans, self.f(l, r, n, s))
        
        return ans