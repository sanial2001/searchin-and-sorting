import heapq


class Solution:
    def kClosest(self, points, k: int):
        pq = []
        for point in points:
            x, y = point
            heapq.heappush(pq, (x ** 2 + y ** 2, point))

        ans = []
        while k > 0:
            dist, point = heapq.heappop(pq)
            ans.append(point)
            if k == 1:
                return ans
            k = k - 1
