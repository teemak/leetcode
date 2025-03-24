# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        curr = dummy

        for i, ll in enumerate(lists):
            if ll:
                heapq.heappush(heap, (ll.val, i, ll))

        while heap:
            val, i, ll = heapq.heappop(heap)
            curr.next = ll
            curr = ll
            ll = ll.next
            if ll:
                heapq.heappush(heap, (ll.val, i, ll))

        return dummy.next