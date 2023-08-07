# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next: 
            return False
        slow, fast = head, head #don't set to equal 
        while fast and fast.next and slow.next: #I do not need to check the fast.next, the 
            #give the fast and slow pointer 
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True 
        else:
            return False 
            
        
        