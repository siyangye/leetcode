class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        deleteBi = False
        max_len = 0
        curr_len = 0
        for i in range(len(nums)):
            if nums[i] == 0 and not deleteBi:
                deleteBi = True
                zero_pos = i
            elif nums[i] == 1:
                curr_len += 1
            elif nums[i] == 0 and deleteBi:
                max_len = max(max_len, curr_len)
                # print(max_len) #3,5
                curr_len = i - zero_pos - 1
                # print(curr_len)#3, 6
                zero_pos = i
        max_len = max(max_len, curr_len)
        if not deleteBi:
            return len(nums) - 1
        else:
            return max_len

