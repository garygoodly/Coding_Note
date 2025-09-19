# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def arr2str(arr):
    return "->".join(map(str, arr))
    return "->".join(arr)   # wrong

class Solution(object):
    def pre_order(self, root, curr_path, ans):
        curr_path += [root.val]
        if root.left == None and root.right == None:
            ans.append(arr2str(curr_path))
            return
        if root.left:
            self.pre_order(root.left, curr_path, ans)
            curr_path.pop()
        if root.right:
            self.pre_order(root.right, curr_path, ans)
            curr_path.pop()

    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root == None:
            return []
        ans = []
        self.pre_order(root, [], ans)
        return ans