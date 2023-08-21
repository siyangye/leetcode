class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, n in enumerate(nums):
            otherNum = target - n
            if otherNum in prevMap:
                return [prevMap[otherNum], i] #the index 
            prevMap[n] = i #add cur n
            
        