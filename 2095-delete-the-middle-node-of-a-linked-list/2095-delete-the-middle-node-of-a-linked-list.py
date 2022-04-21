# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode(next=head)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            
        while head:
            if head.next == slow:
                head.next = head.next.next
                break
            head = head.next
            
        return dummy.next
        