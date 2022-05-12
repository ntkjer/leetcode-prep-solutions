# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def solve(node, subNode):
            if not node and not subNode:
                return True
            if not node or not subNode:
                return False
            return node.val == subNode.val and solve(node.left, subNode.left) and solve(node.right, subNode.right)
            
        
        if solve(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)