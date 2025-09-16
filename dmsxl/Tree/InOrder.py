# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        if root == None:
            return ans

        st = deque()
        curr = root
        while (curr or len(st) > 0):
            while (curr):
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        if root == None:
            return ans

        st = deque()
        curr = root
        while (curr or len(st) > 0):
            while (curr):
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans

    def inorderTraversal(self, root):
        ans = []
        st = deque()
        if root:
            st.append((root, False))
        
        while (st):
            node, visit = st.pop()
            if visit:
                ans.append(node.val)
                continue
            if node.right:
                st.append((node.right, False))
            st.append((node, True))
            if node.left:
                st.append((node.left, False))
        return ans