# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def match(nodeA, nodeB) -> bool:
            if not nodeA and not nodeB:
                return True
            if not nodeA or not nodeB:
                return False

            return (nodeA.val == nodeB.val 
                    and match(nodeA.left, nodeB.left) 
                    and match(nodeA.right, nodeB.right))
        
        if match(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
      