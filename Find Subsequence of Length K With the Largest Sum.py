import heapq


class Solution:
    def maxSubsequence(self, nums, k: int):
        pq = []
        for num in nums:
            heapq.heappush(pq, -num)

        ans = 0
        while k:
            ans += -heapq.heappop(pq)
            k -= 1

        return ans


if __name__ == "__main__":
    print(Solution().maxSubsequence(nums=[2, 1, 3, 3], k=2))
