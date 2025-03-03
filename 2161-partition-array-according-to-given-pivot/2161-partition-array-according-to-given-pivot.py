class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [pivot] * n
        i = 0
        j = n - 1
        for num in nums:
            if num < pivot:
                res[i] = num
                i += 1
            elif num > pivot:
                res[j] = num
                j -= 1
        j += 1
        k = n - 1
        while j < k:
            res[j], res[k] = res[k], res[j]
            j += 1
            k -=1
        return res
