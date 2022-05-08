class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            # print(mid)
            if mid > 0 and mid < len(nums) - 1 and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        return start
