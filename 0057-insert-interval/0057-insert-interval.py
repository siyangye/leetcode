class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        if not intervals:
            res.append(newInterval)
            return res
        if intervals[-1][1]<newInterval[0]:
            intervals.append(newInterval)
            return intervals
        if intervals[0][0]>newInterval[1]:
            res.append(newInterval)
            while i<n:
                res.append(intervals[i])
                i+=1
            return res

        while i < n and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
        #what if i==n??
        if i==n:
            res.append(newInterval)
            return res
        merge = [min(intervals[i][0],newInterval[0]),min(intervals[i][1],newInterval[1])]
        while i < n and intervals[i][0]<=newInterval[1]:
            merge[1]=max(merge[1],intervals[i][1])
            i+=1
        res.append(merge)
        while i < n: #intervals[i][0]> newIntervals[1]
            res.append(intervals[i])
            i+=1
        return res
        
            


