class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -1 * num)

        sums, cnt = sum(nums), 0
        target = sums / 2
        while sums > target:
            # print(sums)
            val = heapq.heappop(pq)
            new_val = val / 2
            heapq.heappush(pq, new_val)
            sums = sums - (-1 * val) + (-1 * new_val)
            cnt += 1

        return cnt
