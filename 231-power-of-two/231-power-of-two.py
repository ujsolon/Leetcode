class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        twoPower = 1
        flag=0
        if n==1:
            return True
        if n<=0:
            return False
        while twoPower<=n and flag==0:
            if n==twoPower:
                flag=1
                return True
            twoPower = twoPower*2
        if flag==0:
            return False
