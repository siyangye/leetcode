class Solution: 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort()
        start=[] 
        end =[] 
        start.append(intervals[0][0]) 
        end.append(intervals[0][1]) 
        res = [] 
        for [i,j] in intervals: 
            if start[-1]<=i<=end[-1] and j > end[-1]: 
                end.pop() 
                end.append(j)
            elif i>end[-1]: 
                start.append(i)
                end.append(j) 
        for i in range(len(start)):
            res.append([start[i],end[i]])
        return res