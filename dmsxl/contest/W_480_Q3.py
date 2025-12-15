class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        neg_idx = 0
        for i, v in enumerate(balance):
            if v < 0:
                neg_idx = i
                break
        
        arr = []

        for i, v in enumerate(balance):
            arr += [balance[(neg_idx + i) % len(balance)]]

        print(arr)

        val = -arr[0]
        ans = 0

        for i in range(1, len(arr) // 2):
            tmp = arr[i] + arr[-i]
            print(i, arr[i], arr[-i], tmp, val)
            if tmp < val:
                ans += tmp * i
                val -= tmp
            else:
                ans += val * i
                val = 0
                
        if val > 0:
            ans = -1

        return ans 