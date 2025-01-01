class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero_list = {}
        # res = []
        # self.array = nums #to access the nums: list[int]
        for i,num in enumerate(nums):
            if num != 0:
                self.nonzero_list[i]= num #{0:1,3:2,4:3}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0 
        # for i in range(len(self.array)):
        #     if self.array[i] != 0:
        #         if vec.array[i] !=0:
        #             res += self.array[i] * vec.array[i]
        # return res 
        for i,num in self.nonzero_list.items():
            if i in vec.nonzero_list:
                res += num * vec.nonzero_list[i]
        return res 
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)