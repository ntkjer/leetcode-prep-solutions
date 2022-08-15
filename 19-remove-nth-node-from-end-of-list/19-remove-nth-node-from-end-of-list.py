# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        
        first = dummy
        second = dummy
        
        for _ in range(n):
            first = first.next
        
        while first and second:
            first = first.next
            second = second.next
        
        curr = dummy
        while curr.next != second:
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next
        