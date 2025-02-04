class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = curr = 0
        right = len(nums) - 1
        while curr <= right:
            if nums[curr] ==0:
                nums[curr],nums[left]=nums[left],nums[curr]
                left+=1
                curr+=1
            elif nums[curr]==1:
                curr+=1
            elif nums[curr]==2:
                nums[right],nums[curr]=nums[curr],nums[right]
                right -= 1
        return   