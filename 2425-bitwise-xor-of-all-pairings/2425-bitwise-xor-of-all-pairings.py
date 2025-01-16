class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Key insight: Each number in nums1 appears len(nums2) times
        # Each number in nums2 appears len(nums1) times
        # If a number appears even times in XOR, it cancels out
        
        result = 0
        
        # If nums2 length is odd, each number in nums1 appears odd times
        # So we need to XOR all numbers in nums1
        if len(nums2) % 2 == 1:
            for num in nums1:
                result ^= num
                
        # If nums1 length is odd, each number in nums2 appears odd times
        # So we need to XOR all numbers in nums2
        if len(nums1) % 2 == 1:
            for num in nums2:
                result ^= num
                
        return result