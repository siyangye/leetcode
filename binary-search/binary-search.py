class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) -1 
        mid = (l + r)//2 
        
        while l <= r:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1 
            mid = (l+r)//2
            
        return -1 


        
        
        