# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {value:idx for idx, value in enumerate(inorder)}
        
        def solve(preorder, inorder):
            if not preorder or not inorder:
                return None
            curr = preorder[0]
            idx = d[curr]
            
            root = TreeNode(curr)
            root.left = self.buildTree(preorder[1: idx + 1], inorder[:idx + 1])
            root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
            return root
        
        res = solve(preorder, inorder)
        return res