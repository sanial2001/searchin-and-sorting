class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            prev, nxt = (mid - 1 + n) % n, (mid + 1) % n
            if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                return nums[mid]
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[mid]
