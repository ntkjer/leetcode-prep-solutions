# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def solve(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return True if p.val == q.val and solve(p.left, q.left) and solve(p.right, q.right) else False
        
        return solve(p, q)