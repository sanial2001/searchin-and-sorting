class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)
        for num in nums:
            sums = sum([int(i) for i in str(num)])
            d[sums].append(num)

        ans = []
        for key in d:
            ans.append(sorted(d[key]))

        res = -1
        for val in ans:
            if len(val) > 1:
                res = max(res, val[-1] + val[-2])

        return res
