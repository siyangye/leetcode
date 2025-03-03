class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        equal = []
        large = []
        res = []
        for num in nums:
            if num < pivot:
                small.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                large.append(num)
        while small:
            curr = small.pop(0)
            res.append(curr)
        while equal:
            curr = equal.pop(0)
            res.append(curr)
        while large:
            curr = large.pop(0)
            res.append(curr)
        return res 