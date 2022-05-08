class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        sorted_nums = sorted(nums)

        for i, val in enumerate(sorted_nums):
            d[val] = d.get(val, i)

        for i in range(len(nums)):
            nums[i] = d[nums[i]]

        return nums
