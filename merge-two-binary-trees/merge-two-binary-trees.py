# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        def solve(nodeA, nodeB):
            if not nodeA:
                return nodeB
            if not nodeB:
                return nodeA

            this_root = TreeNode()
            a_val = nodeA.val if nodeA else 0
            b_val = nodeB.val if nodeB else 0

            this_root.val = a_val + b_val
            this_root.left = solve(nodeA.left, nodeB.left)
            this_root.right = solve(nodeA.right, nodeB.right)

            return this_root

        return solve(root1, root2)
            