import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        pq = []
        for key in d:
            heapq.heappush(pq, (-d[key], key))

        ans = []
        while k > 0:
            cnt, num = heapq.heappop(pq)
            ans.append(num)
            if k == 1:
                return ans
            k = k - 1
