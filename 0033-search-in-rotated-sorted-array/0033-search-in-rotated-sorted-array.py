class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[-1]:
            l = 0
            r = len(nums) - 1
            while l <=r:
                mid = (l+r) //2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
            return -1

        else:
            index = {}
            for i in range(len(nums)):
                index[nums[i]] = i
                if i+1 < len(nums) and nums[i] > nums[i+1]:
                    array = nums[i+1:] + nums[:i+1]
            l = 0
            r = len(array) - 1
            while l <=r:
                mid = (l + r) //2
                if array[mid] == target:
                    res = index[target]
                    return res
                elif array[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
            

