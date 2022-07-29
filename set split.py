class Solution:
    def solve(self, nums):
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        prev_i, prev_j = -1, n
        sums1, sums2 = 0, 0

        while i < j:
            if i > prev_i: sums1 += nums[i]
            if j < prev_j: sums2 += nums[j]
            print(sums1, sums2)
            if nums[i] < nums[j] and j - i == 1 and sums1 == sums2:
                return True
            prev_i, prev_j = i, j
            if sums1 < sums2:
                i += 1
            else:
                j -= 1
        return False
