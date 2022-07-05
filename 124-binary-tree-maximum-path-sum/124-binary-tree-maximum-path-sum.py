# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def solve(node):
            nonlocal res
            if not node:
                return 0
            left = max(0, solve(node.left))
            right = max(0, solve(node.right))
            
            res = max(left + right + node.val, res)
            return node.val + max(left, right)
        
        
        solve(root)
        return res