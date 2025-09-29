# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pre_order(self, root1, root2):
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        root1.val += root2.val
        root1.left = self.pre_order(root1.left, root2.left)
        root1.right = self.pre_order(root1.right, root2.right)
        return root1

    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.pre_order(root1, root2)