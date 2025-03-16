class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        #怎么判断这个时间是可以的
        def canRepair(time):
            curr = 0
            for rank in ranks:
                curr += int(math.sqrt(time / rank))
            return curr >= cars  
        l = 0
        r = min(ranks) * cars * cars
        res = 0
        while l <= r:
            mid = (l +r) //2
            if canRepair(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


            