# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashset = set()
        tempA = headA
        while tempA!=None:
            hashset.add(tempA)
            tempA=tempA.next
        
        tempB = headB
        while(tempB not in hashset):
            try:
                tempB=tempB.next
            except:
                return(None)
        return(tempB)
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempB = headB
        while(tempB!=None):
            tempA = headA
            #print(tempB)
            while(tempA!=tempB and tempA!=None):
                #print(tempA)
                tempA=tempA.next
            if(tempB==tempA):
                #print('yes')
                return(tempB)
            tempB=tempB.next
        
'''