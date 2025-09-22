# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def post_order(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        leftsum = self.post_order(root.left)
        if root.left != None and root.left.left == None and root.left.right == None:
            leftsum += root.left.val
        rightsum = self.post_order(root.right)

        return leftsum + rightsum

    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.post_order(root)