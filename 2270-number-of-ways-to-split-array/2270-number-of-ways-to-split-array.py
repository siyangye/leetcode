class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sums = 0
        prefix =[]
        count = 0
        for i in range(len(nums)):
            sums += nums[i]
            prefix.append(sums)
        for j in range(len(nums)-1):
            if prefix[j]>= sums/2:
                count +=1
        return count
        