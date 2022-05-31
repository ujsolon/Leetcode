'''
import itertools as it

def allkSubstrings(s:str, k:int)->list[str]:
    res = [s[x:y] for x, y in it.combinations(range(len(s) + 1), r = 2) if len(s[x:y]) == k]
    return(res)

def listtostr(l:list)-> str:
    ans=""
    for x in l:
        ans+=x
    return ans

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        base='01'
        binlist = [listtostr(l) for l in list(it.product(base,repeat=k))]
        subssk = allkSubstrings(s,k)
        for x in binlist:
            if not(x in subssk):
                return False
        return True
'''

##below approach just counts number of k length substrings and if this meets the number of all k length binary strings, return True

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:                
            return len({s[i:i+k] for i in range(len(s)-k+1)}) == 2 ** k