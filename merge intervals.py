class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for i, j in intervals[1:]:
            last = ans[-1][1]
            if i <= last:
                ans[-1][1] = max(last, j)
            else:
                ans.append([i, j])

        return ans
