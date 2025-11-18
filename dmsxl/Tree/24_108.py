# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.f(nums, 0, len(nums) - 1)

    def f(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        root.left = self.f(nums, left, mid - 1)
        root.right = self.f(nums, mid + 1, right)
        return root