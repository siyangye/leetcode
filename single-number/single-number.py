class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = 0 
        while n+1 < len(nums):
            if nums[n] == nums[n+1]:
                # del nums[n]
                # del nums[n+1]
                n += 2 
            else:
                return nums[n]
        return nums[n]
        