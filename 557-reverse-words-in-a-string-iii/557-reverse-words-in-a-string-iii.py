def revstring(s):
    return s[::-1]

class Solution:
    def reverseWords(self, s: str) -> str:
        news=""
        for substring in s.split():
            news+=revstring(substring)+" "
        return(news[0:len(news)-1])