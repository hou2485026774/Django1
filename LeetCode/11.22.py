import copy
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.ori = copy.copy(nums)
        self.v = nums

    def reset(self) -> List[int]:
        for i in range(len(self.v)):
            self.v[i] = self.ori[i]
        return self.v

    def shuffle(self) -> List[int]:
        n = len(self.v)
        t = n - 1
        for i in range(n - 1,-1,-1):
            ran = random.randint(0,t)
            self.v[i],self.v[ran] = self.v[ran],self.v[i]
            t -= 1
        return self.v



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()