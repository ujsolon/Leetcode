class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans=[]
        for i in range(len(candies)):
            if (candies[i]+extraCandies >= maxCandies):
                ans.append(True)
            else:
                ans.append(False)
        return(ans)