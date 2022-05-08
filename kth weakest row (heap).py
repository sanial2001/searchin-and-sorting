class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        pq = []

        for i, val in enumerate(mat):
            sums = sum(val)
            heapq.heappush(pq, (sums, i))

        ans = []
        while k > 0:
            sums, i = heapq.heappop(pq)
            ans.append(i)
            k -= 1

        return ans
