# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def solve(node):
            if not node: return
            left, right = node.left, node.right
            node.right = left
            node.left = right
            solve(node.left)
            solve(node.right)
            return node
        
        return solve(root)
        