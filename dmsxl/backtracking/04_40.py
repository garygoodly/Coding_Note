class Solution(object):
    def bt(self, candidates, target_sum, path_sum, ans, path, start_idx):
        if target_sum == path_sum:
            ans.append(path[::])
            return
        
        if path_sum > target_sum:
            return
        
        used = None
        for i in range(start_idx, len(candidates)):
            if used != candidates[i]:
                used = candidates[i]
                path.append(candidates[i])
                path_sum += candidates[i]
                self.bt(candidates, target_sum, path_sum, ans, path, i + 1)
                path.pop()
                path_sum -= candidates[i]


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.bt(candidates, target, 0, ans, [], 0)
        return ans