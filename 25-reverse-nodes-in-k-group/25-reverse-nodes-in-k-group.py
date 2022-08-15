# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseKth(head, k):
            prev = None
            while k:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
                k -= 1
                
            return prev
        
        curr = head
        count = 0
        while count < k and curr:
            curr = curr.next
            count += 1
        
        if count == k:
            rev = reverseKth(head, k)
            head.next = self.reverseKGroup(curr, k)
            return rev
        
        return head