# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def post_order(self, root):
        if root == None:
            return (True, 0)
        left_balanced, left_height = self.post_order(root.left)
        right_balanced, right_height = self.post_order(root.right)
        if left_balanced and right_balanced:
            if abs(left_height - right_height) <= 1:
                return (True, max(left_height, right_height) + 1)
        return (False, -1)
        
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.post_order(root)[0]
    
class Solution(object):
    def post_order(self, root):
        if root == None:
            return 0
        left_height = self.post_order(root.left)
        right_height = self.post_order(root.right)
        if left_height != -1 and right_height != -1:
            if abs(left_height - right_height) <= 1:
                return max(left_height, right_height) + 1
        return -1
        
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.post_order(root) != -1