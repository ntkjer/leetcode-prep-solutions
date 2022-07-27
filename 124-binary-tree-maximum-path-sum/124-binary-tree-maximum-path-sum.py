# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def solve(node):
            nonlocal res
            if not node:
                return 0
            left = max(solve(node.left), 0)
            right = max(solve(node.right), 0)
            
            res = max(res, left + right + node.val)
            
            return max(left, right) + node.val
        
        solve(root)
        return res