class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = 0
        while l <= r:
            mid = (l + r)//2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid != len(nums) -1 and nums[mid] > nums[mid + 1]: #转折
                return nums[mid+1]
            elif nums[mid] > nums[0]:
                l = mid + 1
            elif nums[mid] < nums[0]:
                r = mid
        