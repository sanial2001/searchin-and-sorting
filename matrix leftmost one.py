class Solution:
    def solve(self, matrix):
        if not matrix:
            return -1
        ans = float("inf")
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            start, end = 0, n - 1
            while start <= end:
                mid = (start + end) // 2
                if row[mid] == 1:
                    ans = min(ans, mid)
                    end = mid - 1
                else:
                    start = mid + 1
        return -1 if ans == float("inf") else ans
