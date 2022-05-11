import itertools

class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        return(len(list(itertools.combinations_with_replacement(vowels, n))))