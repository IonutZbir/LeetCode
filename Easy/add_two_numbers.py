# Problem https://leetcode.com/problems/add-two-numbers/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def fromListToListNode(self, l: List, i) -> Optional[ListNode]:
        if i >= len(l):
            return
        return ListNode(l[i], self.fromListToListNode(l, i + 1))
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        r = 0
        l = []
        while node1 != None or node2 != None:
            if node1 == None:
                node1 = ListNode(0)
            if node2 == None:
                node2 = ListNode(0)

            s = node1.val + node2.val + r
            
            if s > 9:
                r = 1
                s = s - 10
            else:
                r = 0

            l.append(s)
            
            node1 = node1.next
            node2 = node2.next
        
        if r == 1:
            l.append(r)

        return self.fromListToListNode(l, 0)
        
s = Solution()

print(s.twoSum([3,2,4], 6))