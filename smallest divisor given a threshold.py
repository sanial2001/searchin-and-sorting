class Solution:
    # Same as koko eating as bananas
    def smallestDivisor(self, nums, t: int) -> int:
        start, end = 1, max(nums)
        ans = 1000000000

        while start <= end:
            mid = (start + end) // 2
            time = 0
            for num in nums:
                time += num // mid if num % mid == 0 else num // mid + 1
            # print(mid, time)
            if time <= t:
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1

        return ans
