# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def solve(node, left=float('-inf'), right=float('inf')):
            if not node:
                return True
            
            if left >= node.val or right <= node.val:
                return False
            
            return solve(node.left, left, node.val) and solve(node.right, node.val, right)
        
        return solve(root)