# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lr_equal(self, left, right):
        if (left == None and right == None):
            return True
        elif (left == None or right == None):
            return False
        elif (left.val != right.val):
            return False
        else:
            return self.lr_equal(left.left, right.right) and self.lr_equal(left.right, right.left)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return True
        return self.lr_equal(root.left, root.right)