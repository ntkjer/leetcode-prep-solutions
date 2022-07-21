# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        # left-most right child of the parenet of p
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor