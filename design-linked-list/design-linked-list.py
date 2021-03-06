class ListNode:
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode()
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length or index < 0:
            return -1
        
        cur = self.head 
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.length, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        
        if index < 0:
            index = 0
        
        pred = self.head
        for _ in range(index):
            pred = pred.next
        
        to_insert = ListNode(val)
        to_insert.next = pred.next
        pred.next = to_insert
        self.length += 1
        return 
            
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length or index < 0:
            return
        
        pred = self.head
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next
        self.length -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)