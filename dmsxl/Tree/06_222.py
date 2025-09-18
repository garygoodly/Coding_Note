# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = right_depth = 1
        node = root
        while (node.left):
            node = node.left
            left_depth += 1
        node = root
        while (node.right):
            node = node.right
            right_depth += 1
        if (left_depth == right_depth):
            return 2 ** left_depth - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)