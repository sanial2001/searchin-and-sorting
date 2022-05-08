class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            # print(grid[i][j])
            if grid[i][j] < 0:
                ans += (m - i)
                j = j - 1
            else:
                i = i + 1

        return ans
