import numpy as np  
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        check=1
        arr = np.array(coins)
        result = np.gcd.reduce(arr)
        ##if sum is not divisible by the gcd of the coins, then no solution
        if amount%result!=0:
            return -1


'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp=[math.inf] * (amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1]==math.inf else dp[-1]