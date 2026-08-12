# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head, curr = None, None
        temp1, temp2 = list1, list2
        while temp1 and temp2:
            if head == None:
                if temp1.val < temp2.val:
                    head = temp1
                    temp1 = temp1.next
                else:
                    head = temp2
                    temp2 = temp2.next
                curr = head
                continue
            if temp1.val < temp2.val:
                curr.next = temp1
                temp1 = temp1.next
            else:
                curr.next = temp2
                temp2 = temp2.next
            curr = curr.next
        
        if temp2 == None:
            curr.next = temp1
        else:
            curr.next = temp2
        
        return head