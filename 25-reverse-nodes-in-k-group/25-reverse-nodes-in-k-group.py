# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseK(node, k):
            """ Given a node: ListNode, and an integer k
                returns k reversed nodes.
            """
            rev = None
            while node and k:
                tmp = node.next
                node.next = rev
                rev = node
                node = tmp
                k -= 1
            return rev
        
        count = 0
        curr = head
        while count < k and curr:
            curr = curr.next
            count += 1
            
        if count == k:
            rev = reverseK(head, k)
            head.next = self.reverseKGroup(curr, k)
            return rev
        
        return head