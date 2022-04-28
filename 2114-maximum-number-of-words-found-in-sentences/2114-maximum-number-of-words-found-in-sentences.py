def numwords(sentence):
    spaces = 0
    lsentence = list(sentence)
    for i in range(len(lsentence)):
        if lsentence[i]==' ':
            spaces+=1
    return (spaces+1)

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([numwords(s) for s in sentences])