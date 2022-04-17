class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringmax = 0
        stringlen = 0
        for i in range(len(s)):
            keystart = i
            substring = []
            while i<=len(s)-1 and s[i] not in substring:
                substring.append(s[i])
                stringlen = len(substring)
                if stringlen >= stringmax:
                    stringmax = stringlen
                i+=1
        return stringmax