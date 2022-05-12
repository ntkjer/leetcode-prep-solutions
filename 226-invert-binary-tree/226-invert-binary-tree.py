# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(node):
            if not node:
                return
            
            if not node.left and not node.right:
                return node
            
            solve(node.right)
            solve(node.left)
            
            node.right, node.left = node.left, node.right
            return node
            
        root = solve(root)
        return root