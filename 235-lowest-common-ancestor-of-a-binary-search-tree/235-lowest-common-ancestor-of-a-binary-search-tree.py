# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def solve(node, p, q):
            if node.val > p.val and node.val > q.val:
                return solve(node.left, p, q)
            elif node.val < p.val and node.val < q.val:
                return solve(node.right, p, q)
            else:
                return node
            
        res = solve(root, p, q)
        return res