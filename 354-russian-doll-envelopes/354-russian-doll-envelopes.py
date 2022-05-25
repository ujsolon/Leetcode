'''
https://leetcode.com/problems/russian-doll-envelopes/discuss/2071640/100-or-0-MS-or-WITH-ANIMATION-or-EPIC-MEME
'''

class Solution:
    def maxEnvelopes(self, E: List[List[int]]) -> int:
        E.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _,height in E:
            left = bisect_left(dp, height)
            if left == len(dp): dp.append(height)
            else: dp[left] = height
        return len(dp)