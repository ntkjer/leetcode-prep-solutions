# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = list()
        def solve(node):
            if not node:
                res.append("None")
                return
            res.append(str(node.val))
            solve(node.left)
            solve(node.right)
        solve(root)   
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
 
        self.idx = 0
        def solve():
            if data[self.idx] == "None" or self.idx >= len(data):
                self.idx += 1
                return None 
            
            curr = TreeNode(data[self.idx])
            self.idx += 1
            curr.left = solve()
            curr.right = solve()
            return curr
        root = solve()
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))