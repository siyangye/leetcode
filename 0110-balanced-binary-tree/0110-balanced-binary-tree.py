# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(curr):
            #base
            if not curr:
                return 0
            #recursive
            l = height(curr.left)
            r = height(curr.right)
            if abs(l -r) > 1 or l == -1 or r == -1: #return -1 if there is a unbalanced child tree
                return -1
            #else
            return max(l, r) + 1
        res = height(root)
        return res != -1
        