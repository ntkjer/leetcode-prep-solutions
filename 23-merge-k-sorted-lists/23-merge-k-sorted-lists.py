# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        
        curr = dummy
        for node in lists:
            while node:
                heappush(heap, node.val)
                node = node.next
        
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
        
        
        return dummy.next
        