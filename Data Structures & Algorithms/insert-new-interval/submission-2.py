class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
# 3. add newInterval to res
# 4. add all remaining intervals to res

        # 1. while intervals[i] ends before newInterval starts: add to res
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2. while intervals[i] still overlaps newInterval: grow newInterval (min of starts, max of ends)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
