class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for s in operations:
            if s=="++X":
                x+=1
            if s=="X++":
                x+=1
            if s=="--X":
                x-=1
            if s=="X--":
                x-=1
        return x