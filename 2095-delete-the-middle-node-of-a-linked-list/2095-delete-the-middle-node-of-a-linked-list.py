# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode(next = head)
        
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        curr = head
        
        while curr:
            if curr.next is slow:
                curr.next = curr.next.next
                break
                
            curr = curr.next
        
        return dummy.next
    