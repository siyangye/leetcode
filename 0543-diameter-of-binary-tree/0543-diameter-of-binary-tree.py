# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def height(node) -> int:
            if not node: #base case
                return 0
            left_height = height(node.left) #sub-left tree
            right_height = height(node.right) #sub-right tree
            node_height = max(left_height,right_height)+1 #including itself
            curr_diameter = left_height + right_height
            nonlocal max_diameter
            max_diameter = max(max_diameter, curr_diameter)
            return node_height

        height(root)
        return max_diameter