# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        while lists:
            curr = lists.pop()
            while curr:
                heappush(pq, curr.val)
                curr = curr.next
                
        dummy = ListNode()
        curr = dummy
        while pq:
            curr.next = ListNode(heappop(pq))
            curr = curr.next
            
        return dummy.next