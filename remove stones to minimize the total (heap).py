class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = []
        for pile in piles:
            heapq.heappush(pq, -1 * pile)

        while k > 0:
            val = heapq.heappop(pq)
            new_val = -1 * val - math.floor((-1 * val) // 2)
            heapq.heappush(pq, -1 * new_val)
            k -= 1

        return sum(pq) * -1