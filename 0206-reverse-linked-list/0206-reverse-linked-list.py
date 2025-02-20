# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        s = []
        while head:
            s.append(head)
            head = head.next
        #no head anymore
        current = end = ListNode(0)
        while s:
            end.next = s.pop()
            end = end.next
            end.next = None
        return current.next


            
            

            