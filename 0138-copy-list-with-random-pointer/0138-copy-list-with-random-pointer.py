"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        ptr = head

        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        ptr_old = head
        ptr_new = head.next
        head_new = head.next

        while ptr_old:
            ptr_old.next = ptr_old.next.next
            ptr_new.next = (ptr_new.next.next if ptr_new.next else None)
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next

        return head_new