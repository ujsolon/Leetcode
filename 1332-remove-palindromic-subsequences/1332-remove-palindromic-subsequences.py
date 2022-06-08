'''
import itertools as it

def listtostr(l:list)-> str:
    ans=""
    for x in l:
        ans+=x
    return ans

def isPalindrome(s:str)->bool:
    return(s==s[::-1])

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        base='ab'
        lnnn=[]
        count=0
        for k in range(1,len(s)+1):
            l = list(it.product(base,repeat=k))
            ln = [listtostr(item) for item in l]
            lnn = [item for item in ln if isPalindrome(item)==True]
            lnnn.append(lnn)
        lnnn.reverse() ##reverse the order of palindromic substrings from the longest to the shortest

        for i in range(len(s)):
            #print(i)
            for string in lnnn[i]:
                #print(string)
                while string in s:
                    #print(string)
                    count+=1
                    s=s.replace(string,'')
        return(count)
'''

##This one liner of a solution takes into account an observation that the max number of steps here is 2, which for me, is not really that immediate
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2