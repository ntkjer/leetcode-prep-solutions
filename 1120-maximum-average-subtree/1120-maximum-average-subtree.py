# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0
        
        def solve(node):
            if not node:
                return (0, 0)
            
            left_sum, left_count = solve(node.left)
            right_sum, right_count = solve(node.right)
            
            size = left_count + right_count + 1
            cur_sum = left_sum + right_sum + node.val
            cur_avg = cur_sum / size
            self.max_avg = max(cur_avg, self.max_avg)
            
            return (cur_sum, size)
             
            
        res = solve(root)
        return self.max_avg