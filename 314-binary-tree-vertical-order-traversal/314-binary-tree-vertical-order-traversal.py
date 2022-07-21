# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return root
        
        columns = {}
        q = collections.deque()
        q.append([root, 0])
        res = list()
        min_col = float('inf')
        max_col = float('-inf')
        
        while q:
            node, column = q.popleft()
            
            if node:
                columns[column] = columns.get(column, []) + [node.val]
                min_col = min(min_col, column)
                max_col = max(max_col, column)
                
                q.append((node.left, column - 1))
                q.append((node.right, column + 1))
                
        return [columns[x] for x in range(min_col, max_col + 1)]