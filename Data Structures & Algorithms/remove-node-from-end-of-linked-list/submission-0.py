# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        if head.next == None:
            return None
        while temp:
            l += 1
            temp = temp.next
        n = l-n
        prev, curr, nex = None, head, head.next
        for i in range(n):
            prev = curr
            curr = nex
            nex = nex.next
        if prev == None:
            head = nex
        else:
            prev.next = nex
        return head