# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = [[]]
        def solve(node, level=0):
            if not node:
                return 
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            solve(node.left, level + 1)
            solve(node.right, level + 1)
            return
        
        solve(root)
        return res
            
            