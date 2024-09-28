class MyCircularDeque:
    class __Node:
        def __init__(self, value: int, left: 'MyCircularDeque.Node', right: 'MyCircularDeque.Node'):
            self.value = value
            self.left = left
            self.right = right
        
        def __str__(self):
            return str(self.value)

    def __init__(self, k: int):
        self.size = k
        self.len_q = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if value == None:
            return False
        
        if self.len_q == self.size:
            return False
        
        node = MyCircularDeque.__Node(value, self.tail, self.head)
        if self.len_q != 0:
            self.head.left = node  
            self.tail.right = node
        else:
            self.tail = node
                    
        self.head = node
        
        self.len_q += 1
        
        return True

    def insertLast(self, value: int) -> bool:
        if value == None:
            return False
        
        if self.len_q == self.size:
            return False
        
        node = MyCircularDeque.__Node(value, self.tail, self.head)
        
        if self.len_q != 0:
            self.head.left = node
            self.tail.right = node
        else:
            self.head = node
        
        self.tail = node
        
        self.len_q += 1
        
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.len_q == 1:
            self.head = None
            self.tail = None
        else:
            new_head = self.head.right
            self.tail.right = new_head
            new_head.left = self.tail
            self.head = new_head
            
        self.len_q -= 1
        
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.len_q == 1:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.left
            self.head.left = new_tail
            new_tail.right = self.head
            self.tail = new_tail
        
        self.len_q -= 1

        return True

    def getFront(self) -> int:
        if self.head != None:
            return self.head.value
        return -1

    def getRear(self) -> int:
        if self.tail != None:
            return self.tail.value
        return -1

    def isEmpty(self) -> bool:
        return self.len_q == 0

    def isFull(self) -> bool:
        return self.len_q == self.size

    def __str__(self):
        result = []
        node = self.head
        i = 0
        while node != None and i < self.len_q:
            result.append(str(node))
            node = node.right
            i += 1
        return "Queue: [ " + ' '.join(result) + " ]"


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()