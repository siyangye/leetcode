# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #find all child node, if there is non-null node after a null node -> not a balanced BST - how to write this logic? - store the child node for all node even the null node? (do a BFS - check all node - store node from top-bottom, left to right ) -> but how to check if there is any non-null node after a null node exist? 
        queue = deque([root])
        null_starting_point = False
        while queue:
            node = queue.popleft()
            if node.left:
                if null_starting_point:
                    return False
                else:
                    queue.append(node.left)
            elif not node.left: #node.left is null
                null_starting_point = True
            if node.right:
                if null_starting_point:
                    return False
                else:
                    queue.append(node.right)
            elif not node.left: #node.left is null
                null_starting_point = True
        return True 


        