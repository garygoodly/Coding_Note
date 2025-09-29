# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, root, val):
        if root == None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.traversal(root.left, val)
        return self.traveral(root.right, val)

    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        return self.traversal(root, val)