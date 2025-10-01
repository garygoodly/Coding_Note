# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        insert_node = TreeNode(val)
        if root == None:
            return insert_node
        prev = None
        curr = root
        while (curr != None):
            prev = curr
            if (val < curr.val):
                curr = curr.left
            else:
                curr = curr.right
        if val < prev.val:
            prev.left = insert_node
        else:
            prev.right = insert_node
        return root