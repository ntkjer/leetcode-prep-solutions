# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = {}
        q = collections.deque()
        q.append([root, 0])
        res = list()
        
        while q:
            node, column = q.popleft()
            
            if node:
                columns[column] = columns.get(column, []) + [node.val]
                
                q.append([node.left, column - 1])
                q.append([node.right, column + 1])
        
        return [columns[x] for x in sorted(columns.keys())]