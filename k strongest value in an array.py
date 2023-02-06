class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        pq = []

        for num in arr:
            heapq.heappush(pq, (-1 * abs(num - median), -1 * num))

        res = []
        while k > 0:
            val, num = heapq.heappop(pq)
            res.append(-1 * num)
            k -= 1

        return res
