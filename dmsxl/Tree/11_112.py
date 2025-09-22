# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preOrder(self, root, pathSum, targetSum, flag):
        if flag:
            return flag
        if root == None:
            return False
        
        pathSum += root.val
        if root.left == None and root.right == None:
            if pathSum == targetSum:
                return True
            return False
        
        flag |= self.preOrder(root.left, pathSum, targetSum, flag)
        flag |= self.preOrder(root.right, pathSum, targetSum, flag)

        return flag
            
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        return self.preOrder(root, 0, targetSum, False)
        