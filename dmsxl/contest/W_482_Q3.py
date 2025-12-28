class Solution(object):
    def onlyfactor(self, m):
        k = m
        ans = defaultdict(int)
        for i in range(2, m // 2 + 1):
            while (k % i == 0):
                ans[i] += 1
                k /= i

        if len(ans) == 0:
            ans[m] += 1
        return ans

    def allonegenerate(self, k):
        return (10 ** k - 1) / 9

    def prime_minallonemulti(self, k):
        n = 1
        for i in range(1, k + 1):
            if n % k == 0:
                return i
            n *= 10
            n += 1
        return -1

    def minAllOneMultiple(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0:
            return -1
        if k % 5 == 0:
            return -1
        onlyFactor = self.onlyfactor(k)
        print(onlyFactor)
        
        for key, val in onlyFactor.items():
            if key == k:
                return k if self.allonegenerate(k) % k == 0 else k - 1
            break


        n = 1
        for i in range(1, k + 1):
            if n % k == 0:
                return i
            n *= 10
            n += 1
        return -1