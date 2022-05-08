import heapq


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        '''
        nums = []
        n = len(arr)
        for i in range(n):
            nums.append([abs(arr[i]-x), arr[i]])
        nums.sort(key=lambda x:x[0])
        ans = []
        for i in range(k):
            ans.append(nums[i][1])
        return sorted(ans)
        '''
        n = len(arr)
        nums = [abs(arr[i] - x) for i in range(n)]
        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i], arr[i]))
        ans = []
        while pq and k > 0:
            diff, num = heapq.heappop(pq)
            ans.append(num)
            k = k - 1
        return sorted(ans)
