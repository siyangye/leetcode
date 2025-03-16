class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        #dict to recrod num and its inddex
        array = {}
        for i in range(len(nums)):
            array[nums[i]] = i
        print(array)
        s_nums = sorted(nums)
        def checkCapability(j:int) -> bool:
            # if j not in nums:
            #     return False
            curr_num = s_nums[mid]
            ind = array[curr_num]
            count = 0
            while ind >= 0:
                if nums[ind] <= curr_num:
                    count += 1
                    ind -= 2
                else:
                    ind -= 1
            ind = array[curr_num]
            while ind < len(nums):
                if nums[ind] < curr_num:
                    count += 1
                    ind += 2
                else:
                    ind += 1
            return count >= k 
        #check avail
        l = 0
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) //2
            if checkCapability(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        print(res)
        return s_nums[res]


                
