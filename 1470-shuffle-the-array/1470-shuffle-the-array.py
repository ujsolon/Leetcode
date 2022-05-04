class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[0:n]
        nums2 = nums[n:2*n]
        nums3 = []
        for i in range(n):
            nums3.append(nums1[i])
            nums3.append(nums2[i])
        return (nums3)