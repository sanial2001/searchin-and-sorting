class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0

        while i < j:
            sums = people[i] + people[j]
            if sums <= limit:
                ans += 1
                i, j = i + 1, j - 1
            elif sums > limit:
                ans += 1
                j = j - 1

        ans += 1 if i == j else 0

        return ans
