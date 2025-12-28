class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        if need1 > need2:
            need1, need2 = need2, need1
            cost1, cost2 = cost2, cost1

        need2 = need2 - need1
        ans = need1 * min(cost1 + cost2, costBoth)
        ans += need2 * min(cost2, costBoth)

        return ans