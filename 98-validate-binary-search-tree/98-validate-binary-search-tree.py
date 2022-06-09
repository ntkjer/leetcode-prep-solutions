# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(node, lo=float('-inf'), hi=float('inf')):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            
            return solve(node.left, lo, node.val) and solve(node.right, node.val, hi)
                
            
            
        
        return solve(root)
        