# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #check if there is a cycle or not: fast & slow pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        #if there is a cycle, find the pointer:
        pointer = head
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next
        #pointer == fast:
        return pointer 
        
        