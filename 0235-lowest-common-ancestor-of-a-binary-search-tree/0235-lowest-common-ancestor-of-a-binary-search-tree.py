# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            if root == p or root == q:
                return root
            if p.val > root.val and q.val > root.val:
                root = root.right
            if p.val < root.val < q.val or q.val < root.val < p.val:
                return root
            if p.val < root.val and q.val < root.val:
                root = root.left
        # if not root:
        #     return None
