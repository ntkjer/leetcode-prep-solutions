class ListNode:
    """
    Doubly linked-list.
    """
    def __init__(self, key=None, val=None, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
    
    def _delete(self, node: ListNode):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def _insert(self, node: ListNode):
        prev, nxt = self.right.prev, self.right
        prev.next = node 
        node.next = nxt
        node.prev = prev
        nxt.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._delete(self.cache[key])
        self._insert(self.cache[key]) # updates most recent
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
            #del self.cache[key]
            
        node = ListNode(key, value)
        self._insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            # leftmost node is going to be evicted
            evictedNode = self.left.next
            self._delete(evictedNode)
            del self.cache[evictedNode.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)