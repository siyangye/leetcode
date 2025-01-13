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
        first = None
        last = None
        def helper(node):
            nonlocal first,last
            if not node:
                return True
            #recursive
            helper(node.left)
            if not first:
                first = node
                last = node
            else:
                last.right = node
                node.left = last
                last = node
            helper(node.right)
        helper(root)
        first.left = last
        last.right = first
        return first
        