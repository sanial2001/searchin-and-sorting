class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        left = [arr[0] for _ in range(n)]
        right = [arr[n - 1] for _ in range(n)]

        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], arr[i])
        right.append(100000000000)

        ans = 0
        for i in range(n):
            if left[i] <= right[i + 1]:
                ans = ans + 1
        return ans
