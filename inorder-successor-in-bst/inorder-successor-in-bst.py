# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.prev = None
        self.inorder_successor = None

        def inorder_traverse(root, p):
            if not root:
                return
            left = inorder_traverse(root.left, p)
            if self.prev == p and not self.inorder_successor:
                self.inorder_successor = root
                return
            self.prev = root
            right = inorder_traverse(root.right, p)

        def solve(root, p):
            if p.right:
                leftmost = p.right
                while leftmost.left:
                    leftmost = leftmost.left
                self.inorder_successor = leftmost
            else:
                inorder_traverse(root, p)

        def solve_optimal(root, p):
            """
            Tn = O(lg n), as this takes advantage of BST property.
            Above solutions are O(n) and work for general binary trees.
            """
            while root:
                if p.val >= root.val:
                    root = root.right
                else:
                    self.inorder_successor = root
                    root = root.left

        #solve(root, p)        
        solve_optimal(root, p)
        return self.inorder_successor

            