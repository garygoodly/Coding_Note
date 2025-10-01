# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def LCA(self, root, l, r):
        if root == None:
            return None
        
        if l <= root.val and root.val <= r:
            return root
        if root.val < l:
            return self.LCA(root.right, l, r)

        return self.LCA(root.left, l, r)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        l, r = min(p.val, q.val), max(p.val, q.val)


        return self.LCA(root, l, r)

