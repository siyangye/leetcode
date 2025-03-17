class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        #lower = nums[0]
        #upper = nums[-1]
        if len(nums) == 0:
            return [[lower, upper]]
        missing_ranges = []   
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])
        for i in range(len(nums) -1):
            if nums[i] + 1 == nums[i + 1]:
                continue
            else:
                missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])
        if nums[-1] < upper:
            missing_ranges.append([nums[-1] + 1, upper]) 
        return missing_ranges



             
                

        