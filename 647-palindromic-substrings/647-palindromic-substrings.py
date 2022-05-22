def allSubstrings(s: str):
    res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    return res

def isPalindrome(s: str) -> bool:
    return s == s[::-1]

class Solution:
    def countSubstrings(self, s: str) -> int:
        subs = allSubstrings(s)
        return sum([1 for item in subs  if isPalindrome(item)])