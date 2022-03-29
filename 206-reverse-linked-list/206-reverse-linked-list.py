# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = None
        while head:
            tmp = head.next
            head.next = tail
            dummy.next = head
            tail = head
            head = tmp
            
        return dummy.next