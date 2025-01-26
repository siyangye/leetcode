import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy=head=ListNode()
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i,l))
        while heap:
            val,i,l = heapq.heappop(heap)
            head.next = l
            head = head.next
            l = l.next
            if l:
                heapq.heappush(heap,(l.val,i,l))
        return dummy.next
                