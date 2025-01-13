"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        last = None
        first = None
        def inOrder(node):
            nonlocal last,first
            if not node:
                return 
            #first, process left child node:
            inOrder(node.left)
            #then process current node:
            if not first:
                first = node
                last = node 
            else:
                last.right = node
                node.left = last
                last = node 
            #lastly, process right child node:
            inOrder(node.right)
        #by the end of the entire recursive, I need to close the circle by connecting first and last node: 
        inOrder(root)
        first.left = last
        last.right = first 
        return first
        



        