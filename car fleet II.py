class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = []
        nums = sorted(zip(position, speed), reverse=True)

        for x, y in nums:
            time.append((target - x) / y)

        ans, prev = 0, 0
        for i in range(n):
            if time[i] > prev:
                ans += 1
                prev = time[i]

        return ans
