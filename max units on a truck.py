class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for box, unit in boxTypes:
            b = min(box, truckSize)
            ans += b * unit
            truckSize -= b
            if truckSize == 0:
                break
        return ans
