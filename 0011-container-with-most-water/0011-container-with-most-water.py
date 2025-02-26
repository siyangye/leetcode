class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            width = r - l
            curr_height = min(height[r], height[l])
            curr_water = width * curr_height
            max_water = max(curr_water,max_water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water
            
