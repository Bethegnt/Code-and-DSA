# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        while(head):
            heappush(heap,head.val)
            head = head.next
        sorted = ListNode(0,None)
        dummy = sorted
        while(heap):
            sorted.val = heappop(heap)
            if(heap):
                sorted.next = ListNode(None)
            sorted = sorted.next
        return dummy
        