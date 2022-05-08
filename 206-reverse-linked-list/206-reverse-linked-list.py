# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        temp = head
        result = temp
        while head:
            values.append(head.val)
            head = head.next
        while temp:
            temp.val = values.pop()
            temp = temp.next
        return result
            