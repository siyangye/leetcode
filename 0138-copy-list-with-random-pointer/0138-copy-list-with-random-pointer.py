"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # new = Node(head.val)
        placeholder = head
        # placeholder = new
        node_dict={}
        while head:#eg,1,2,3,4
            node_dict[head]=Node(head.val)#eg,1:node(1),2:node(2),3:node(3),4:node(4)
            head=head.next
        head=placeholder 
        while head:
            if head.next:
                node_dict[head].next=node_dict[head.next]#dict:node:new_node or val:new_node
                # print(new.next.val)
            if head.random:
                node_dict[head].random=node_dict[head.random]
                # print(head.random.val)
            head=head.next
            # new=new.next
        return node_dict[placeholder]
        