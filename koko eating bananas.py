class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        start, end = 1, max(piles)
        ans = 10000000000000
        while start <= end:
            mid = (start + end) // 2
            time = 0
            for pile in piles:
                time += pile // mid if pile % mid == 0 else pile // mid + 1
            # print(mid, time)
            if time <= h:
                ans = min(ans, mid)
                end = mid - 1
            elif time > h:
                start = mid + 1
        return ans
