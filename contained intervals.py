class Solution:
    def solve(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: [x[0], -x[1]])
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if x >= res[-1][0] and y <= res[-1][1]:
                continue
            else:
                res.append([x, y])
        return len(intervals) - len(res)
