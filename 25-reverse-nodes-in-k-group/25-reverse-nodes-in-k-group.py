# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseKth(head, k):
            new, curr = None, head
            while k:
                tmp = curr.next
                curr.next = new
                new = curr
                curr = tmp
                k -= 1
            return new
        
        count = 0
        curr = head
        while count < k and curr:
            curr = curr.next
            count += 1
        
        if count == k:
            rev = reverseKth(head, k)
            head.next = self.reverseKGroup(curr, k)
            return rev
        
        return head