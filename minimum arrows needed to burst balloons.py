class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda x: x[1])
        ans, curr = 1, points[0]

        for i in range(len(points)):
            if points[i][0] > curr[1]:
                ans += 1
                curr = points[i]

        return ans
