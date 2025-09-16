# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    # def preorderTraversal_Helper(self, root, arr):
    #     if root == None:
    #         return
    #     arr.append(root.val)
    #     self.preorderTraversal_Helper(root.left, arr)
    #     self.preorderTraversal_Helper(root.right, arr)
    #     return

    # def preorderTraversal(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
    #     ans = []
    #     self.preorderTraversal_Helper(root, ans)
    #     return ans
    
    
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        if root == None:
            return ans

        st = deque()
        st.append(root)
        while (len(st) > 0):
            curr = st.pop()
            ans.append(curr.val)
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
        return ans