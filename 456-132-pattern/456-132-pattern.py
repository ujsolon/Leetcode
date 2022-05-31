'''
def removeRepeating(l:list)->list:
    return([v for i, v in enumerate(l) if i == 0 or v != l[i-1]])

class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        if len(set(nums))<3:
            return(False)
        nums = removeRepeating(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[k] and nums[k]< nums[j]:
                        return(True)
        return(False)

'''

##https://leetcode.com/problems/132-pattern/discuss/2015125/Python-Solution-using-Stack

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        second_num = -math.inf
        stck = []
        # Try to find nums[i] < second_num < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_num:
                return True
            # always ensure stack can be popped in increasing order
            while stck and stck[-1] < nums[i]:
                second_num = stck.pop()
            stck.append(nums[i])
        return False
        

