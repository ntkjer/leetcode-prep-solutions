# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def solve(node, depth=0):
            if not node:
                return depth
            
            if not node.left and not node.right:
                return 1 + depth
            
            return 1 + max(solve(node.left, depth), solve(node.right, depth))
        
        return solve(root, 0)