class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        n = len(nums)
        count, max_count = 1, 0
        if n == 1:
            return 1

        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                count = count + 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count


if __name__ == '__main__':
    print(Solution().findLengthOfLCIS([1]))
