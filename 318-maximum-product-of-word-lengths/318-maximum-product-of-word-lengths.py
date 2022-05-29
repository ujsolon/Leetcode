def strSameCharQ(string1: str, string2: str)->bool:
    hashset = []
    for char in string1:
        hashset.append(char)
    for char in string2:
        if char in hashset:
            return True
    return False

def listtostr(l:list)-> str:
    ans=""
    for x in l:
        ans+=x
    return ans

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordsuniq = [listtostr(set(x)) for x in words]
        ans=0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ##use wordsuniq to check a common char
                if not strSameCharQ(wordsuniq[i], wordsuniq[j]) and (len(words[i])*len(words[j]))>ans:
                    ans=len(words[i])*len(words[j])
        return ans