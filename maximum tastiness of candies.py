class Solution:
    def check(self, nums, x, k):
        n = len(nums)
        i, j, cnt = 0, 1, 1
        while cnt < k and j < n:
            # print(nums[j], nums[i])
            if nums[j] - nums[i] >= x:
                cnt += 1
                i = j
            j += 1
        return cnt == k

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        start, end = 0, max(price)
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            # print(mid)
            if self.check(price, mid, k):
                ans = max(ans, mid)
                start = mid + 1
            else:
                end = mid - 1
        return ans
