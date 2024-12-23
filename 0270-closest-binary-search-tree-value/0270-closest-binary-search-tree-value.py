# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_res = float('inf')
        res = float('inf')
    #如果相等min_res 或者小于 都要存储，但是存法不一样
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            curr_diff = abs(node.val - target)
            if curr_diff < min_res:
                min_res = curr_diff
                res= node.val
            if curr_diff == min_res:
                res = min(res,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res 
        