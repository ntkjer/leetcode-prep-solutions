# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {value:idx for idx, value in enumerate(inorder)}
        
        def recur(preorder, inorder):
            if not preorder or not inorder:
                return None
            val = preorder[0]
            root = TreeNode(val)
            mid = d[val]
            root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
            return root
        
        res = recur(preorder, inorder)
        return res