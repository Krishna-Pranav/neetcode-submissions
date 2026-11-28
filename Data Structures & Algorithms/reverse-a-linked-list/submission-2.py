# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        h1, h2 = head, head.next
        h1.next = None
        while h2:
            h3 = h2.next
            h2.next = h1
            h1 = h2
            h2 = h3
        return h1