class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = 0
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > nums[0]:
                l = mid + 1
            elif nums[mid] <= nums[0]:
                res = nums[mid]
                r = mid - 1
        return res