'''
Bit manipulation solution
https://leetcode.com/problems/number-of-1-bits/discuss/2076914/Bit-Manipulation-oror-Python-Solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            if n&1==1: ##bitwise operator
                count+=1
            n=n>>1 ##bitwise shift operators
        return count
'''
def intToDigits(x):
    return ([int(item) for item in list(str(x))])

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(intToDigits('{:032b}'.format(n)))