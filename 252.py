# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True
        intervals.sort(cmp=None, key=lambda x:x.start, reverse=False)
        pre = intervals[0].end
        for interval in intervals[1:]:
            if interval.start<pre:
                return False
            pre = interval.end
        return True