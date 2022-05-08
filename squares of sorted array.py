class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i, j = 0, len(nums) - 1

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res = [nums[i] ** 2] + res
                i = i + 1
            else:
                res = [nums[j] ** 2] + res
                j = j - 1

        return res
