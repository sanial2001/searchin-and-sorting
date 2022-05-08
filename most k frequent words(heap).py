class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1

        pq = []
        for key in d:
            heapq.heappush(pq, (-d[key], key))

        ans = []
        while k > 0:
            cnt, word = heapq.heappop(pq)
            ans.append(word)
            k = k - 1

        return ans
