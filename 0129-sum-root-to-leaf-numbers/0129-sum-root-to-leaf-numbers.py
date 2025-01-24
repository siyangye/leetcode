# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0 
        queue = deque([(root,0)])

        while queue:
            node,curr = queue.popleft()
            if not node.left and not node.right:
                curr_val = curr+node.val
                total+=curr_val
                continue
            inc= (curr+node.val)*10
            if node.left:
                queue.append((node.left,inc))
            if node.right:
                queue.append((node.right,inc))
        return total