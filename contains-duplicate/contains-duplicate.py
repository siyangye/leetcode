class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n =0
        while n+1 <len(nums):
            if nums[n] == nums[n+1]:
                return True 
            n += 1 
        return False 
        