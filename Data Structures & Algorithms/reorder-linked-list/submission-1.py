# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if head == None or head.next == None or head.next.next == None:
        #     return head
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        if n < 3:
            return
        temp = head
        for i in range(math.ceil(n/2)):
            prev = temp
            temp = temp.next
        prev.next = None
        prev, curr = None, temp
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        temp = head
        a, b = temp, prev
        while prev:
            temp2 = temp.next
            temp.next = prev
            prev2 = prev.next
            prev.next = temp2
            temp = temp2
            prev = prev2
