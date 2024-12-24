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
        #use DFS to find all parent, and make two list
        # use two pointer to point to the highest parent, and move to the lower side to find the lowest common ancestor. 
        def AllAncestor(p: 'Node') -> list: #or maybe deque? 
            parent = collections.deque([])
            res =collections.deque([p])
            
            while res:
                node = res.popleft()
                parent.append(node)
                if node.parent:
                    res.append(node.parent)
            return parent
            
        p_par= AllAncestor(p)
        q_par= AllAncestor(q)
        # go through p,q from right, until p!= q 
        curr_lca = p_par[-1] #init the root val as the comoon ancestor
        while p_par and q_par:
            curr_p = p_par.pop()
            curr_q = q_par.pop()
            if curr_p == curr_q:
                curr_lca = curr_p #update lca  
            else:
                return curr_lca
        return curr_lca

        

                
            
        