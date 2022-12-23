class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        for u, v in intervals:
            if pq and pq[0] < u:
                heapq.heappop(pq)
            heapq.heappush(pq, v)
        return len(pq)
