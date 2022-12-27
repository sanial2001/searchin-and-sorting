class Solution:
    def check(self, nums, x, k):
        n = len(nums)
        i, j, cnt = 0, 1, 1
        while cnt < k and j < n:
            if nums[j] - nums[i] >= x:
                i = j
                cnt += 1
            j += 1
        return cnt == k

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = 0
        start, end = 0, max(position)
        while start <= end:
            mid = (start + end) // 2
            if self.check(position, mid, m):
                ans = max(ans, mid)
                start = mid + 1
            else:
                end = mid - 1
        return ans
