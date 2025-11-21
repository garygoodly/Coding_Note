class Solution(object):
    def bt(self, target_sum, path_sum, candidates, ans, path, start_idx):
        if path_sum > target_sum:
            return
        if path_sum == target_sum:
            ans.append(path[:])
            return
        n = len(candidates)
        for i in range(start_idx, n):
            path.append(candidates[i])
            path_sum += candidates[i]
            self.bt(target_sum, path_sum, candidates, ans, path, i)
            path.pop()
            path_sum -= candidates[i]

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.bt(target, 0, candidates, ans, [], 0)
        return ans