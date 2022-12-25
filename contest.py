import collections
import math


class Solution:
    def countAnagrams(self, s):
        items = s.split(' ')
        res = 1
        for item in items:
            den = 1
            n = len(item)
            count = collections.Counter(item)
            print(count.items())
            for key in count:
                if count[key] > 1:
                    den *= math.factorial(count[key])
            res *= math.factorial(n)//den
        print(res%(10**9 + 7))


if __name__ == "__main__":
    Solution().countAnagrams("b okzojaporykbmq tybq zrztwlolvcyumcsq jjuowpp")
