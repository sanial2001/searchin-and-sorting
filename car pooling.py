class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pick, drop = [], []
        for trip in trips:
            pick.append([trip[0], trip[1]])
            drop.append([trip[0], trip[2]])
        pick.sort(key=lambda x: x[1])
        drop.sort(key=lambda x: x[1])

        i, j = 0, 0
        n = len(trips)
        total = 0
        while i < n or j < n:
            if total > capacity:
                return False
            if i < n and pick[i][1] < drop[j][1]:
                total += pick[i][0]
                i += 1
            else:
                total -= drop[j][0]
                j += 1

        return True
