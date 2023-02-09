class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -1 * num)

        sums = 0
        while k > 0:
            val = heapq.heappop(pq)
            sums += -1 * val
            new_val = math.ceil(-1 * val / 3)
            heapq.heappush(pq, -1 * new_val)
            k -= 1

        return sums
