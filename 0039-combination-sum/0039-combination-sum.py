class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(ind,path,total):
            if ind >= len(nums):
                return
            elif total > target:
                return
            elif total ==target:
                res.append(path.copy())
                return
            path.append(nums[ind])
            dfs(ind,path,total+nums[ind])
            path.pop()
            dfs(ind+1,path,total)


        dfs(0, [], 0)
        return res