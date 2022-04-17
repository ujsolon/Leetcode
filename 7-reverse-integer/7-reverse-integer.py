class Solution:
    def reverse(self, myInt: int) -> int:
        if myInt <= -2**31-1 or myInt >= 2**31:
            ans=0
        else:
            if myInt <0:
                myIntpos = abs(myInt)
                s = str(myIntpos)
                ans = -int(s[::-1])
            else:
                s = str(myInt)
                ans = int(s[::-1])
        if ans <= -2**31-1 or ans >= 2**31:
            ans=0
        return ans