import itertools as it
import math

def listTOint(l):
    s = [str(integer) for integer in l]
    a_string = "".join(s)
    res = int(a_string)
    return res

def digits(x:int):
    return [int(item) for item in list(str(x))]

class Solution:
    def minimumSum(self, num: int) -> int:
        l = list(it.permutations(digits(num)))
        minsum = math.inf
        for item in l:
            newsum = listTOint(item[:1]) + listTOint(item[1:])
            if newsum<minsum:
                minsum=newsum
            newsum = listTOint(item[:2]) + listTOint(item[2:])
            if newsum<minsum:
                minsum=newsum
        return(minsum)
        