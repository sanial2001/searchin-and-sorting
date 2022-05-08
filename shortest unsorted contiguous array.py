class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = n - 1, 0

        prev = nums[0]
        for i in range(1, n):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        nxt = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > nxt:
                start = i
            else:
                nxt = nums[i]

        return 0 if end == 0 else (end - start + 1)
