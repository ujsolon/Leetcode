'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        chars = set(s)
        charsk = [x*k for x in chars]
        len1 = len(s)
        len2 = 0
        while len1!=len2:
            len1=len(s)
            for item in charsk:
                s=s.replace(item, '')
            len2=len(s)
        return(s)
'''

##https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/2079402/python-solution

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
                if(stack[-1][1] == k):
                    stack.pop()
            else:
                stack.append([i , 1])
                
            
        stack = [char * count for char , count in stack]  
        return "".join(stack)