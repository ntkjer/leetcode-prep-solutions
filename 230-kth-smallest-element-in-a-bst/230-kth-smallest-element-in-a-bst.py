# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        # preorder traversal and then heappush?
        stack = [root]
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            heappush(pq, node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        res = None
        for _ in range(k):
            res = heappop(pq)
        return res