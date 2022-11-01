class Solution:
    def split(self, candies, mid, k):
        res = 0
        for i in candies:
            res += i // mid
        return res

    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 1, 10 ** 7
        res = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            split = self.split(candies, mid, k)
            # print(split)
            if split >= k:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res
