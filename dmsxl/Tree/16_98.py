# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def __init__(self):
        self.pre = None
        self.max_val = float('-inf')

    def post_order(self, root, is_bst, subtree_min, subtree_max):
        if root == None:
            return True, subtree_min, subtree_max
        if root.left == None and root.right == None:
            return True, root.val, root.val
        if is_bst == False:
            return False, 0, 0
        left_is, left_min, left_max = self.post_order(root.left, is_bst, subtree_min, subtree_max)
        right_is, right_min, right_max = self.post_order(root.right, is_bst, subtree_min, subtree_max)
        if left_is == False or right_is == False:
            return False, 0, 0
        if not left_max < root.val:
            return False, 0, 0
        if not root.val < right_min:
            return False, 0, 0
        return True, min(left_min, root.val), max(right_max, root.val)

    def in_order(self, root):
        if root == None:
            return True
        left = self.in_order(root.left)
        if left:
            if self.max_val < root.val:
                self.max_val = root.val
            else:
                return False
            right = self.in_order(root.right)
            return right
        return False

    def in_order(self, root):
        if root == None:
            return True
        left = self.in_order(root.left)
        if self.pre != None and not self.pre.val < root.val:
            return False
        self.pre = root
        right = self.in_order(root.right)
        return left and right

    def in_order(self, root):
        if root == None:
            return True
        left = self.in_order(root.left)
        if left:
            if self.pre != None:
                if not self.pre.val < root.val:
                    return False
            self.pre = root
            right = self.in_order(root.right)
            return right
        return False

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.in_order(root)