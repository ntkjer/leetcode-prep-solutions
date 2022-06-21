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
        
        res = 0
        for _ in range(1, k + 1):  
            res = heappop(heap)
        return res