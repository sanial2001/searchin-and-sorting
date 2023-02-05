class Solution:
    def check(self, nums, mid, cnt, k):
        i, n = 0, len(nums)
        while i < n:
            if nums[i] <= mid:
                i += 2
                cnt += 1
            else:
                i += 1
            if cnt == k:
                return True
        if cnt < k:
            return False

    def minCapability(self, nums: List[int], k: int) -> int:
        start, end = min(nums), max(nums)
        while start < end:
            mid = (start + end) // 2
            if self.check(nums, mid, 0, k):
                end = mid
            else:
                start = mid + 1
        return start
