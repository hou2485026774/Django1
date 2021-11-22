from itertools import combinations


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        l = ['a','b','c']
        l1 = []
        # for i in s1:
        #     l.append(i)
        for i in combinations(l,r):
            print(i)
        return True
test = Solution()
s1 = "ab"
s2 = "eidbaooo"
test.checkInclusion(s1,s2)