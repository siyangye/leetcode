class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            if i+1 < n and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        for num in nums:
            if num != 0:
                res.append(num)
        while len(res) < n:
            res.append(0)
        return res
        
        