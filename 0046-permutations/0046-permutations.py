class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_res = []
        def dfs():
            if len(curr_res) == len(nums):
                res.append(curr_res[:])#append copy of curr_res, cuz list is mutable
                return
            #recursive case:
            for i in nums:
                if i not in curr_res:
                    curr_res.append(i)
                    dfs() 
                    curr_res.pop()#so that we go back to the for loop again, do another dfs
        dfs()
        return res
            