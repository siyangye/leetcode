class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # n = 0 
        # while n+1 < len(nums):
        #     if nums[n] == nums[n+1]:
        #         # del nums[n]
        #         # del nums[n+1]
        #         n += 2 
        #         #don't delete element while iterating the length of the array 
        #     else:
        #         return nums[n]
        # return nums[n]
        
        hashSet = set()
        for n in nums:
            if n in hashSet:
                hashSet.remove(n)
            else: 
                hashSet.add(n)
        return hashSet.pop()
            
        