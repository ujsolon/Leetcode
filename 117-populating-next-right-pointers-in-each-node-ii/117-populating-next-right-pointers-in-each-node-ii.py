"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()
        q.append(root)
        dummy=Node(-999) # to initialize with a not null prev
        while q:
            length=len(q) # find level length
            
            prev=dummy
            for _ in range(length): # iterate through all nodes in the same level
                popped=q.popleft()
                if popped.left:
                    q.append(popped.left)
                    prev.next=popped.left
                    prev=prev.next
                if popped.right:
                    q.append(popped.right)
                    prev.next=popped.right
                    prev=prev.next                
                 
        return root
'''
from
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/2033286/Python-Easy%3A-BFS-and-O(1)-Space-with-Explanation

I was able to do an in-level approach, but iterating the code over each level was too much for me

def flatten(t):
    return [item for sublist in t for item in sublist]

def subroots(root):
    return([root.left, root.right])

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        uproot = [root]
        downroot = subroots(root)
        for i in range(len(downroot)-1):
            downroot[i].next = downroot[i+1]
        
        uproot = downroot
        downroot = [subroots(x) for x in downroot]
        lendown = len(downroot)
        downroot = flatten(downroot)
        if len(downroot) == 0:
            return(root)
        
        for i in range(len(downroot)-2):
            counter=1
            while downroot[i+counter]==None:
                counter+=1
            downroot[i].next = downroot[i+counter]
            
        return(root)

'''