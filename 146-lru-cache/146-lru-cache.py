class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _delete(self, node: Node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        
    def _insert(self, node: Node):
        prv, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prv
        prv.next, nxt.prev = node, node
        
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._delete(self.cache[key])
        self._insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
            
        curr = Node(key, value)
        self._insert(curr)
        self.cache[key] = curr
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._delete(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)