# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current=dummy
        carry=0

        while l1 or l2 or carry!=0:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            curr_val=carry+val1+val2
            curr_digit = curr_val%10
            carry= curr_val//10
            print(curr_digit)

            l1=l1.next if l1 else l1
            l2=l2.next if l2 else l2

            current.next=ListNode(curr_digit)
            current=current.next
        return dummy.next
        



        
        