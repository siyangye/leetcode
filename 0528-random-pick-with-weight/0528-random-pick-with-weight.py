class Solution:

    def __init__(self, w: List[int]):
        #get prefix sum 
        self.prefix = []
        self.sum = 0
        for i in w:
            self.sum+= i
            self.prefix.append(self.sum)

    def pickIndex(self) -> int:
        l=0
        r = len(self.prefix)-1
        target = random.randint(1, self.sum)
        
        while l < r: #l<=r
            mid = (l+r)//2
            if self.prefix[mid] < target:
                l=mid+1
            else:
                r=mid
        return l

        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()