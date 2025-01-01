class Solution:
    def maxScore(self, s: str) -> int:
        zeros = {}
        ones = {}
        max_score = 0
        r = 0 
        l = 0
        for i in range(len(s)-1):
            if s[i]=='0':
                r+= 1
            if s[-i-1]=='1':
                l+= 1
            zeros[i] = r
            ones[len(s)-1-i-1]=l
        print(zeros)
        print(ones)
        for j in range(len(s)-1):
            print(j)
            curr_score = zeros[j] + ones[j]
            max_score = max(max_score, curr_score)
            print(max_score)
        return max_score

        


