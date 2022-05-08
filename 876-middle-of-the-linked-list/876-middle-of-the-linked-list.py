# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenll = 0
        headtemp = head
        while headtemp:
            lenll+=1
            headtemp = headtemp.next
        if lenll%2==1:
            mid = int((lenll-1)/2)
            for i in range(mid):
                head = head.next
            return(head)    
        else:
            mid = int((lenll)/2)
            for i in range(mid):
                head = head.next
            return(head)