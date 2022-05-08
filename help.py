class Solution:
    def binary_search(self, nums, target):
        start, end = 0, len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return -1

    def find(self, nums):
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            print(mid)
            prev, nxt = (mid - 1 + n) % n, (mid + 1) % n
            if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                return mid
            elif nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid - 1

    def search(self, nums, target: int) -> int:
        n = len(nums)
        if nums[0] <= nums[n - 1]:
            return self.binary_search(nums, target)

        min_index = self.find(nums)
        print(min_index)
        x1 = self.binary_search(nums[:min_index], target)
        return x1 if x1 != -1 else self.binary_search(nums[min_index:], target)


if __name__ == "__main__":
    Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
