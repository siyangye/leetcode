class ListNode:
    def __init__(self,val,next,prev):
        self.val, self.next, self.prev = val, next, prev
    
class MyCircularQueue:

    def __init__(self, k: int):
        #initialize a empty linked list with the size of k & create dummy node on left/ right side:
        self.queueSize = k #empty linked list  
        self.l = ListNode(0, None, None)
        self.r = ListNode(0, None, self.l)
        self.l.next = self.r 
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            #do something
            cur = ListNode(value, self.r, self.r.prev)
            self.r.prev.next = cur
            self.r.prev = cur 
            #update queue size:
            self.queueSize -= 1
            return True 
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            #do something
            self.l.next = self.l.next.next
            self.l.next.prev = self.l
            #update queue size:
            self.queueSize += 1
            return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.l.next.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.r.prev.val

    def isEmpty(self) -> bool:
        return self.l.next == self.r

    def isFull(self) -> bool:
        return self.queueSize == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()