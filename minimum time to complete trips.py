class Solution:
    def total_trips(self, time, t, k):
        trips = 0
        for i in time:
            trips += t // i
        return trips

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, 10 ** 15
        res = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            trips = self.total_trips(time, mid, totalTrips)
            if trips >= totalTrips:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return res
