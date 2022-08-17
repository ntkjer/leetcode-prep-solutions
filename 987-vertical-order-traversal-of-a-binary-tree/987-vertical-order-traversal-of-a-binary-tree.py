# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        columns = {}
        q = collections.deque()
        max_level = 0
        min_level = 0
        
        q.append((root, 0, 0))
        nodes = list()
        
        
        while q:
            node, col, level = q.popleft()
            
            if not node:
                continue
            
            nodes.append([col, level, node.val])
            
            q.append((node.left, col - 1, level + 1))
            q.append((node.right, col + 1, level + 1))
        
        nodes.sort()
        res = {}
        
        for col, level, val in nodes:
            res[col] = res.get(col, []) + [val]
        
        return res.values()
        
        
        
        
        
        