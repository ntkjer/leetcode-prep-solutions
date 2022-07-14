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
        
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            carry = 0
            if tmp >= 10:
                carry = tmp // 10
                tmp = tmp % 10
                
            curr.next = ListNode(tmp)
            curr = curr.next
            l1, l2 = l1.next, l2.next
            
        l3 = l1 or l2
        while l3:
            tmp = l3.val + carry
            carry = 0
            if tmp >= 10:
                carry = tmp // 10
                tmp = tmp % 10
            curr.next = ListNode(tmp)
            curr = curr.next
            l3 = l3.next
            
        if carry:
            curr.next = ListNode(1)
            curr = curr.next
            
        return dummy.next