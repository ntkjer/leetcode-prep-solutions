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
        q.append((root, 0, 0))
        
        min_col, max_col = 0, 0
        nodes = list()
        while q:
            
            node, col, row = q.popleft()
            
            if not node: 
                continue
            
            nodes.append((col, row, node.val))
            q.append((node.left, col - 1, row + 1))
            q.append((node.right, col + 1, row + 1))
            
        nodes.sort()
        node_dict = {}
        
        for col, row, value in nodes:
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            
            node_dict[col] = node_dict.get(col, []) + [value]
        
        res = list()
        for i in range(min_col, max_col + 1):
            res.append(node_dict[i])
            
        return res