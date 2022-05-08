class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        for i in range(n):
            mx = (2 ** i) * nums[i]
            mn = (2 ** (n - 1 - i)) * nums[i]
            ans += (mx - mn)

        return ans % (10 ** 9 + 7)
