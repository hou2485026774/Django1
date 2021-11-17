from itertools import combinations
from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        res = int(len(candyType)/2)
        anser = []
        for i in combinations(candyType,res):
            anser.append(len(set(i)))
            # print(i)
        return max(anser)