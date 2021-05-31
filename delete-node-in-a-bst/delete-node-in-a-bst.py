# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # find predecessor and successor
        
        def find_successor(root):
            root = root.right
            while root.left:
                root = root.left
            return root.val
        
        def find_predecessor(root):
            root = root.left
            while root.right:
                root = root.right
            return root.val
        
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            # if not leaf check either left or right child
            # set current root value as successor or predecessor
            # and then recursively delete either its successor or predecessor
            elif root.right:
                root.val = find_successor(root)
                root.right = self.deleteNode(root.right, root.val) 
            else:
                root.val = find_predecessor(root)
                root.left = self.deleteNode(root.left, root.val)


        return root
            