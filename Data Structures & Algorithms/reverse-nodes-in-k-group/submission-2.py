# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotate(self, head, k):
        prev, curr = head, head.next
        while curr and k-1:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            k -= 1
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        while temp:
            temp2 = temp.next
            temple, i = temp2, k-1
            while temple and i:
                temple = temple.next
                i -= 1
            if not temple:
                break
            next_grp = temple.next
            temp.next = self.rotate(temp2, k)
            temp2.next = next_grp
            temp = temp2
        return dummy.next