# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        columns = {}
        q = collections.deque()
        
        q.append((root, 0))
        min_range = 0
        max_range = 0
        
        while q:
            node, level = q.popleft()
            
            if not node:
                continue
            
            columns[level] = columns.get(level, []) + [node.val]
            
            min_range = min(min_range, level)
            max_range = max(max_range, level)
            
            q.append((node.left, level - 1))
            q.append((node.right, level + 1))
            
        res = list()
        for i in range(min_range, max_range + 1):
            res.append(columns[i])
            
        return res