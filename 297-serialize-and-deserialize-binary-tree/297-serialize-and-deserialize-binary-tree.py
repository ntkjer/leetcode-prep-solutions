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
        
        def dfs(node):
            if not node:
                res.append("Nil")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.index = 0
        nodes = data.split(",")
        def dfs():
            if nodes[self.index] == "Nil":
                self.index += 1
                return None
            curr = TreeNode(int(nodes[self.index]))
            self.index += 1
            curr.left = dfs()
            curr.right = dfs()
            return curr
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))