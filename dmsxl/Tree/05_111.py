# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        min_height = 1
        if root.left and root.right:
            min_height = min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left:
            min_height = self.minDepth(root.left) + 1
        elif root.right:
            min_height = self.minDepth(root.right) + 1
        return min_height
      
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        min_depth = 1
        q = deque([root])

        while len(q):
            num_node_layer = len(q)
            for _ in range(num_node_layer):
                node = q.popleft()
                if node.left == None and node.right == None:
                    return min_depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            min_depth += 1
        
        return min_depth
