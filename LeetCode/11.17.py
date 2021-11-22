from itertools import combinations
from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #combinations 排列组合
        res = []
        def test(a,b):
            for i in a:
                if i in b:
                    return False
            return True
        for j in combinations(words,2):#两两组合 排列组合
            print(j)
            if test(j[0],j[1]):
                res.append(len(j[0])*len(j[1]))
        return max(res)

test = Solution()
words = ["a","ab","abc","d","cd","bcd","abcd"]
print(test.maxProduct(words))
u = {}
u['username']=111
u['password'] = 222
print(u)