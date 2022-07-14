class Node:
    # Doubly linked-list
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.left = Node() # LRU
        self.right = Node() # MRU
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {} 
    
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def _insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        
        if len(self.cache) > self.size:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)