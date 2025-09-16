from collections import deque
class Solution(object):
    # def postorderTraversal_Helper(self, root, arr):
    #     if root == None:
    #         return
    #     self.postorderTraversal_Helper(root.left, arr)
    #     self.postorderTraversal_Helper(root.right, arr)
    #     arr.append(root.val)
    #     return

    # def postorderTraversal(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
    #     ans = []
    #     self.postorderTraversal_Helper(root, ans)
    #     return ans
    
    def postorderTraversal(self, root):
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
            if curr.left:
                st.append(curr.left)
            if curr.right:
                st.append(curr.right)

        ans.reverse()
        return ans
    
    def PostorderTraversal(self, root):
        ans = []
        st = deque()
        if root:
            st.append((root, False))
        
        while (st):
            node, visit = st.pop()
            if visit:
                ans.append(node.val)
                continue
            st.append((node, True))
            if node.right:
                st.append((node.right, False))
            if node.left:
                st.append((node.left, False))

        return ans