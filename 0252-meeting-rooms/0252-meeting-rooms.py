class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)<= 1:
            return True
        intervals.sort(key=lambda x: x[0])
        curr_end = intervals[0][-1]
        for interval in intervals[1:]:
            if interval[0] < curr_end:
                return False
            else:
                curr_end = interval[1]
        return True

