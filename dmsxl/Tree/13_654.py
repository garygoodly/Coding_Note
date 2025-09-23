# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pre_order(self, nums, idx_begin, idx_end):
        if idx_end == idx_begin:
            return None
        if idx_end - idx_begin == 1:
            return TreeNode(nums[idx_begin])
        
        max_idx = idx_begin
        for idx in range(idx_begin + 1, idx_end):
            if nums[idx] > nums[max_idx]:
                max_idx = idx
        root = TreeNode(nums[max_idx])
        left_itvl_begin = idx_begin
        left_itvl_end = max_idx
        right_itvl_begin = max_idx + 1
        right_itvl_end = idx_end

        root.left = self.pre_order(nums, left_itvl_begin, left_itvl_end)
        root.right = self.pre_order(nums, right_itvl_begin, right_itvl_end)
        return root

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.pre_order(nums, 0, len(nums))