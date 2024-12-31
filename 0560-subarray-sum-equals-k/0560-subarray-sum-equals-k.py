class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        prefix = {0:1}
        count = 0
        for num in nums:
            sums += num
            if sums - k in prefix:
                count += prefix[sums-k]
            prefix[sums] = prefix.get(sums,0) +1 #存入dict的方式
        return count



