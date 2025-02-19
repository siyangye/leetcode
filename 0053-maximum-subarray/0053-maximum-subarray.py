class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            if current_sum <0:
                current_sum = num
            else:
                current_sum += num
            # current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum
#run time： O(n)
# space : O(1)