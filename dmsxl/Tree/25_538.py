# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.value = 0
        pass

    def in_order(self, root):
        if root == None:
            return
        self.in_order(root.right)
        root.val += self.value 
        self.value = root.val
        self.in_order(root.left)

        return 

    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.in_order(root)
        return root