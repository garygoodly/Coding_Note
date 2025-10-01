# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.prev = None
        self.max_freq = 0
        self.now_freq = 0

    def inorder(self, root, ans):
        if root == None:
            return
        self.inorder(root.left, ans)
        if self.prev == None:
            self.now_freq = 1
        else:
            if root.val == self.prev.val:
                self.now_freq += 1
            else:
                self.now_freq = 1
        if self.now_freq > self.max_freq:
            # ans = [root.val]                # Don't do this, it'll locally change, while the recall one isn't changed.
            ans[:] = []
            ans += [root.val]
            self.max_freq = self.now_freq
        elif self.now_freq == self.max_freq:
            ans += [root.val]

        self.prev = root
        self.inorder(root.right, ans)

    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = []
        self.inorder(root, ans)
        return ans