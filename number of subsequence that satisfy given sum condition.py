class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        end = len(nums) - 1
        nums.sort()
        for i in range(len(nums)):
            while nums[i] + nums[end] > target:
                if end > i:
                    end = end - 1
                else:
                    return res % (10 ** (9) + 7)
            res += pow(2, end - i)
        return res % (10 ** (9) + 7)

        '''
        nums.sort()
        n = len(nums)
        j = n-1
        res = 0
        for i in range(n):
            while nums[i] + nums[j] > target:
                if j > i:
                    j -= 1
                else:
                    return res % (10**9 + 7)
            res += pow(2, j-i)
        return res % (10**9 + 7)
        '''


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0

        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res += pow(2, j - i)
                i += 1

        return res % (10 ** 9 + 7)
