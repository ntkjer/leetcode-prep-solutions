# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def traverse(node):
            if not node:
                return
            heappush(heap, node.val)
            traverse(node.left)
            traverse(node.right)
            return
        
        traverse(root)
        
        for _ in range(k - 1):
            heappop(heap)
            
        return heap[0]