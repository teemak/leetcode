# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            colsum = l1val + l2val + carry
            carry = colsum // 10
            newNode = ListNode(colsum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None    
            l2 = l2.next if l2 else None    
        
        return dummy.next