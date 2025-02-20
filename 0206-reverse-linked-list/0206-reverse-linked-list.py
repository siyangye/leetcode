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
            end.next = None #这个地方很容易错！这样才能打破旧的next pointer关系！
        return current.next


            
            

            