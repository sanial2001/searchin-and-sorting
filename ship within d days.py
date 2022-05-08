class Solution:
    def split(self, nums, total):
        i, sums = 0, 0
        days = 1
        while i < len(nums):
            sums += nums[i]
            if sums > total:
                sums = nums[i]
                days += 1
            i += 1
        return days

    def shipWithinDays(self, weights, days: int) -> int:
        start, end = max(weights), sum(weights)
        possible_days, ans = -1, -1

        while start <= end:
            mid = (start + end) // 2
            possible_days = self.split(weights, mid)
            if possible_days <= days:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans
