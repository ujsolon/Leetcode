'''
import itertools

class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        return(len(list(itertools.combinations_with_replacement(vowels, n))))
'''

## lexicographically sorted usally makes use of the itertools package, either using it.permutations or it.combinations_with_replacement
## this solution uses the factorial form
import math
m=5
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return(int(math.factorial(m+n-1)/(math.factorial(n)*math.factorial(m-1))))