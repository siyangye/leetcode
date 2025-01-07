class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        max_heights = 0
        res = []
        for i in range(n-1,-1,-1):
            if heights[i]>max_heights:
                res.append(i)
                max_heights = heights[i]
        return sorted(res)
            