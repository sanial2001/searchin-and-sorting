class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        ans = []
        n = len(items)
        for i in range(1, n):
            items[i][1] = max(items[i][1], items[i - 1][1])

        for q in queries:
            res = 0
            start, end = 0, n - 1
            while start <= end:
                mid = (start + end) // 2
                if items[mid][0] <= q:
                    res = max(res, items[mid][1])
                    start = mid + 1
                else:
                    end = mid - 1
            ans.append(res)

        return ans
