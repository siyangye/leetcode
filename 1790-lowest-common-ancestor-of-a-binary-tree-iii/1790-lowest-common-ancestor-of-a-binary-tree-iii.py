"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def get_ancestors(node:'Node') -> list:
            ancestors = []
            while node:
                ancestors.append(node)
                node = node.parent 
            return ancestors
        p_ancestors = get_ancestors(p)
        q_ancestors = get_ancestors(q)
        lca = None 
        while p_ancestors and q_ancestors:
            p_curr = p_ancestors.pop()
            q_curr = q_ancestors.pop()
            if p_curr != q_curr:
                break
            lca = p_curr
        return lca

