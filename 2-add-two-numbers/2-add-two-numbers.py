# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        dummy = ListNode(next=node)
        carry = 0
        
        while l1 and l2:
            
            curr = l1.val + l2.val + carry

            if curr >= 10:
                carry = 1
            else:
                carry = 0
                
            curr = ListNode(curr % 10)
            
            node.next = curr
            
            node = node.next
            
            l1, l2 = l1.next, l2.next
        
        while l1:
            curr = l1.val + carry
            if curr >= 10:
                carry = 1
            else:
                carry = 0
            curr = ListNode(curr % 10)
            node.next = curr
            node = node.next
            l1 = l1.next
            
        while l2:
            curr = l2.val + carry
            if curr >= 10:
                carry = 1
            else:
                carry = 0
            curr = ListNode(curr % 10)
            node.next = curr
            node = node.next
            l2 = l2.next
        
        if carry:
            node.next = ListNode(1)
            node = node.next
        
        return dummy.next.next