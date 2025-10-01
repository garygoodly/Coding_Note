# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev = None
        self.min = 10**5
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)

        if self.prev != None:
            self.min = min(self.min, root.val - self.prev.val)

        self.prev = root
        self.inorder(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.inorder(root)
        return self.min