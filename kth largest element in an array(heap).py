import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num * -1)

        while k > 0:
            res = heapq.heappop(pq)
            if k == 1:
                return res * -1
            k = k - 1
