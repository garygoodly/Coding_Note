"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        max_dep = 1
        for child in root.children:
            max_dep = max(max_dep, self.maxDepth(child) + 1)
        return max_dep