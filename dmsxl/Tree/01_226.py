# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def preorderTraversal_Helper(self, root):
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.preorderTraversal_Helper(root.left)
        self.preorderTraversal_Helper(root.right)
        return

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.preorderTraversal_Helper(root)
        return root

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return root
        
        q = deque()    
        q.append(root)

        while (len(q)):
            num_node = len(q)
            for _ in range(num_node):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root