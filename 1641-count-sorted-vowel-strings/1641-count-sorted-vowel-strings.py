'''
import itertools

class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        return(len(list(itertools.combinations_with_replacement(vowels, n))))
'''

import math
m=5
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return(int(math.factorial(m+n-1)/(math.factorial(n)*math.factorial(m-1))))