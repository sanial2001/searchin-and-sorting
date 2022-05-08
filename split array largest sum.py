class Solution:
    def split(self, nums, total):
        i = 0
        split = 1
        sums = 0
        while i < len(nums):
            sums += nums[i]
            if sums > total:
                sums = nums[i]
                split += 1
            i += 1
        return split

    def splitArray(self, nums, m: int) -> int:
        start, end = max(nums), sum(nums)
        possible_split, ans = -1, -1
        while start <= end:
            mid = (start + end) // 2
            possible_split = self.split(nums, mid)
            # print(mid, possible_split)
            if possible_split <= m:
                end = mid - 1
                ans = mid
            else:
                start = mid + 1

        return ans
