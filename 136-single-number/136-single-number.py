class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums)>=1:
            currnum = nums[0]
            nums.remove(currnum)
            if currnum in nums:
                nums.remove(currnum)
            else:
                return currnum