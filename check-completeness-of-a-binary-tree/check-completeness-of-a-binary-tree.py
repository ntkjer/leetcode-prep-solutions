# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = collections.deque()
        q.append(root)
        should_end = False
        while q:
            curr = q.popleft()
            if not curr:
                should_end = True
            elif curr and should_end:
                return False
            else:
                q.append(curr.left)
                q.append(curr.right)

        return True
            