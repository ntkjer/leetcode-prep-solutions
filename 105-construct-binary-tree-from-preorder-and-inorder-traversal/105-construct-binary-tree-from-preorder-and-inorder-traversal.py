# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
            
        def solve(preorder, inorder):
            if not preorder or not inorder:
                return
            val = preorder[0]
            curr = TreeNode(val)
            idx = inorder_map[val]
            curr.left = self.buildTree(preorder[1: idx + 1], inorder[:idx + 1])
            curr.right = self.buildTree(preorder[idx + 1: ], inorder[idx + 1: ])
            return curr
        
        root = solve(preorder, inorder)
        return root