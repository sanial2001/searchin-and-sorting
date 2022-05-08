class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left = [nums[0] for _ in range(n)]
        right = [nums[n - 1] for _ in range(n)]

        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        right.append(float("inf"))

        for i in range(n):
            if left[i] <= right[i + 1]:
                return i + 1
