# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return []
    
        ans = []
        q = deque()
        q.append(root)

        while (len(q)):
            num_node = len(q)
            layer = []
            for _ in range(num_node):
                node = q.popleft()
                layer.append(node.val)
                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
            ans.append(layer)
    
        return ans
    