# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        q = collections.deque()
        q.append((root, 0))
        res = [[]]
        
        while q:
            curr, level = q.popleft()
            
            if not curr:
                continue
            
            if level >= len(res):
                res.append([])
            
            q.append((curr.left, level + 1))
            q.append((curr.right, level + 1))
            
            res[level].append(curr.val)
        
        return res