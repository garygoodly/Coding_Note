# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def traversal(self, inorder, postorder, in_begin, in_end, po_begin, po_end, index_table):
        if po_end - po_begin == 0:
            return None
        if po_end - po_begin == 1:
            # print(postorder[po_begin])
            return TreeNode(postorder[po_begin])
        root = TreeNode(postorder[po_end - 1])
        # print(root.val)
        inorder_root_index = index_table[postorder[po_end - 1]]
        in_left_begin = in_begin
        in_left_end = inorder_root_index
        in_right_begin = inorder_root_index + 1
        in_right_end = in_end
        po_left_begin = po_begin
        po_left_end = po_begin + inorder_root_index - in_begin
        po_right_begin = po_begin + inorder_root_index - in_begin
        po_right_end = po_end - 1

        # print(in_left_begin, in_left_end)
        # print(po_left_begin, po_left_end)
        # print(in_right_begin, in_right_end)
        # print(po_right_begin, po_right_end)
        # print(postorder_left_interval, postorder_right_interval)
        root.left = self.traversal(inorder, postorder, in_left_begin, in_left_end, po_left_begin, po_left_end, index_table)
        root.right = self.traversal(inorder, postorder, in_right_begin, in_right_end, po_right_begin, po_right_end, index_table)
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        index_table = {}
        for idx, num in enumerate(inorder):
            index_table[num] = idx
        return self.traversal(inorder, postorder, 0, len(inorder), 0, len(postorder), index_table)
