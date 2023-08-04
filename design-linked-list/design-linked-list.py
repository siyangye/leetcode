#initiate a node
class ListNode:   
    def __init__(self, val):        
        self.val = val        
        self.next = None
        self.prev = None

class MyLinkedList: 
    def __init__(self):
        #dummy node:
        self.left = ListNode(0) 
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        cur = self.left.next 
        while cur and index > 0: 
            cur = cur.next
            index  -= 1
        #go out of bound:
        if cur and cur!=self.right and index == 0:
            return cur.val
        else:
            return -1 #can I write this way 
        

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next =  node
        node.prev = prev 
        node.next = next
        next.prev = node 
        
    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right 
        prev.next = node
        node.prev = prev 
        node.next = next
        next.prev = node 

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, prev, next = ListNode(val), cur.prev, cur #do I need self? 
            prev.next = node
            node.prev = prev 
            node.next = next
            next.prev = node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur !=self.right and index == 0: #bounds 
            prev, next = cur.prev, cur.next  #do I need self? 
            prev.next = next
            next.prev = prev 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)