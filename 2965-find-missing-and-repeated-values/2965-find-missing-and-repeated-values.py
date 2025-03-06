class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set()
        new_nums = set()
        ans = []
        for i in range(1, n**2 +1):
            nums.add(i)
        for i in range(n):
            for j in range(n):
                curr = grid[i][j]
                if curr in new_nums:
                    ans.append(curr)
                else: #curr not in new_nums
                    nums.remove(curr)
                    new_nums.add(curr)
        ans.append(nums[0])
        return ans
        
                
        