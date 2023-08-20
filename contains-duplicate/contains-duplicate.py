class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # I. use array:
        # nums.sort()
        # n =0
        # while n+1 <len(nums):
        #     if nums[n] == nums[n+1]:
        #         return True 
        #     n += 1 
        # return False 
        
        #II. use hash set: 
        hashset = set()
        for num in nums:
            if num in hashset:
                return True 
            hashset.add(num)
        return False 
        