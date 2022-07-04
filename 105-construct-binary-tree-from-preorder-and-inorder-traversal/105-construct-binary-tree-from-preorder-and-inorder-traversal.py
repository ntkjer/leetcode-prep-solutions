# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        
        def solve(pre, ino):
            if not pre or not ino:
                return None
            
            curr = TreeNode(pre[0])
            idx = inorder_map[pre[0]]
            
            curr.left = self.buildTree(pre[1:idx + 1], ino[:idx])
            curr.right = self.buildTree(pre[idx + 1:], ino[idx + 1:])
        
            return curr
        
        res = solve(preorder, inorder)
        return res