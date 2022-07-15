# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float('-inf')
        
        def solve(node):
            if not node:
                return 0
            left = max(solve(node.left), 0)
            right = max(solve(node.right), 0)
            
            self.result = max(self.result, left + right + node.val)
            
            return max(left, right) + node.val
        

        solve(root)
        return self.result