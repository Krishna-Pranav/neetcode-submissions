"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        d = {}
        temp = head
        while temp:
            val = Node(temp.val)
            d[temp] = val
            temp = temp.next
        
        for key in d.keys():
            if key.next != None:
                d[key].next = d[key.next]
            if key.random != None:
                d[key].random = d[key.random]
        return d[head]