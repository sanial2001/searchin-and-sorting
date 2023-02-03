class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if sum(skill) % (n // 2) != 0:
            return -1
        target = sum(skill) // (n // 2)
        skill.sort()
        prev = skill[0] + skill[n - 1]
        res = skill[0] * skill[n - 1]
        i, j = 1, n - 2

        while i < j:
            val = skill[i] + skill[j]
            if val != prev:
                return -1
            res += skill[i] * skill[j]
            i, j = i + 1, j - 1
        return res
