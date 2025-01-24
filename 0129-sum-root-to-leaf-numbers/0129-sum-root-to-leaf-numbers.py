# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0 
        def dfs(node: TreeNode,curr:int) -> int:
            if not node:
                return
            curr= curr * 10 + node.val 
            if not node.left and not node.right:
                self.total += curr
                return
            # if node.left:
            #     dfs(node.left,curr)
            # if node.right:
            #     dfs(node.right,curr)
            dfs(node.left,curr)
            dfs(node.right,curr)
        dfs(root,0)
        return self.total 

        