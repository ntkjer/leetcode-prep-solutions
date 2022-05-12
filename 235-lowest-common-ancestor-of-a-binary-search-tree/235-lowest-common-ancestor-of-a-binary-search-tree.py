# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        res = None
        while stack:
            node = stack.pop()

            if p.val < node.val and q.val < node.val:
                if node.left:
                    stack.append(node.left)
            elif p.val > node.val and q.val > node.val:
                if node.right:
                    stack.append(node.right)
            else:
                return node
            
        return None