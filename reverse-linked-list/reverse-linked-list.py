# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#method1:iteratively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next #save next value
            cur.next = prev 
            prev = cur  #move to next node
            cur = nxt #move to the next node 
        #break: curr is None 
        return prev #the head of the reversed linked list 

#method2:recursively