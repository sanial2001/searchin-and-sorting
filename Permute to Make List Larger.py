class Solution:
    def solve(self, a, b):
        n = len(a)
        a.sort(reverse=True)
        b.sort(reverse=True)

        i, j = 0, 0
        ans = 0
        while i < n and j < n:
            while j < n and b[j] >= a[i]:
                j += 1
            if j == n:
                break
            ans += 1
            i, j = i + 1, j + 1

        return ans
