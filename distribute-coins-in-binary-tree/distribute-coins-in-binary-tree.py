# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.result = 0

        def solve(node):
            if not node:
                return 0
            left, right = solve(node.left), solve(node.right)
            self.result += abs(left) + abs(right) 
            return node.val + left + right - 1 

        solve(root)
        return self.result
        