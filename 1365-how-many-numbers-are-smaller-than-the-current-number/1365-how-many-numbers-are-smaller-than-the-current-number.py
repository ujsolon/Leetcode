class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter=0
        counterlist=[]
        for i in range(len(nums)):
            counter = len([x for x in nums if x<nums[i]])
            counterlist.append(counter)
        return(counterlist)