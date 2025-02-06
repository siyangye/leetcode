class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
                
            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                # 如果target在左半部分的范围内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 往左找
                else:
                    left = mid + 1   # 往右找
            # 右半部分有序
            else:
                # 如果target在右半部分的范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 往右找
                else:
                    right = mid - 1  # 往左找
        return -1