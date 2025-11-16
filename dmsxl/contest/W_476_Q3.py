class Solution(object):
    def countDistinctFull(self, digits, n):
        if (n < 10 ** (digits - 1)):
            return 0
        if (digits == 1):
            return n
        m = n
        digits = 0
        msb = 0
        while (m > 0):
            digits += 1
            msb = m % 10
            m //= 10
        remain = n % (10 ** (digits - 1))
        ans = ((msb - 1) * 9 ** (digits - 1) + self.countDistinctFull(digits - 1, remain))
        return ans

    def countDistinct(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n < 10):
            return n
        m = n
        digits = 0
        msb = 0

        while (m > 0):
            digits += 1
            msb = m % 10
            m //= 10
        remain = n % (10 ** (digits - 1))
        if remain == 0 and msb == 1:
            return 9 * (9 ** (digits - 1) - 1) // 8 if digits > 1 else 0
        
        ans = self.countDistinct(10**(digits - 1)) + (msb - 1) * 9 ** (digits - 1) + self.countDistinctFull(digits - 1, remain)
        return ans

