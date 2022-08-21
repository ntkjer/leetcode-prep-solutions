class Node:
    """
    A doubly linked node. 
    Initialized to point prev and next to None.
    """
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next
        
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.items = {}
        self.left = Node() # LRU 
        self.right = Node() # MRU
        self.left.next = self.right
        self.right.prev = self.left

    def _insert(self, node: Node):
        prv, nxt = self.right.prev, self.right.next
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node
        
        
    def _remove(self, node: Node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
    
    
    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        
        # get the node and update as MRU         
        node = self.items[key]
        self._remove(node)
        self._insert(node)
        return self.items[key].val
        
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self._remove(self.items[key])
            
        node = Node(key, value)
        self.items[key] = node
        self._insert(node)
        
        if len(self.items) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.items[lru.key]
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)