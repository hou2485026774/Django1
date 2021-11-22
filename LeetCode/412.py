from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = ['FizzBuzz','Fizz','Buzz']
        res = []
        for i in range(1,n+1):
            if i%(3*5)==0:
                res.append(l[0])
            elif i%3==0:
                res.append(l[1])
            elif i%5==0:
                res.append(l[2])
            else:
                res.append(str(i))
        return res
test = Solution()
print(test.fizzBuzz(3))