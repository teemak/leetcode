import heapq

def mergeK(lists):
    heap = []
    dummy = ListNode()
    current = dummy
    
    for i, ll in enumerate(lists):        
        if ll:
            heapq.heappush(heap, (ll.val, i, ll))
            
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = node
        node = node.next
        if node:
            heapq.heappush(heap, (node.val, i, node))            
    return dummy.next
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

lists = [create_linked_list([2,6]), create_linked_list([1,3,4]), create_linked_list([1,4,5])]
# lists = [[1,4,5], [1,3,4], [2,6]]

print(mergeK(lists))
