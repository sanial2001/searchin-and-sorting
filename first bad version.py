# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans = n
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid) == True:
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
        return ans
