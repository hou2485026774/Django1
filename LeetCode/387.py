import collections
from collections import Counter


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         s1 = collections.Counter(s)
#         l = []
#         for i in s1.items():
#             if i[1]==1:
#                 l.append(s.index(i[0]))
#
#         if len(l)==0:
#             return -1
#         else:
#             return l[0]
# test = Solution()
# s = "loveleetcode"
# print(test.firstUniqChar(s))
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         for i in t:
#             if t.count(i)!=s.count(i):
#                 return i
# test = Solution()
# s = "a"
# t = "aa"

# print(test.findTheDifference(s,t))
from typing import List


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         return 1
#
# digits = [9]
# res = ''
# for i in digits:
#     res+= str(i)
# print(list(str(int(res)+1)))

#67
# a = "11"
# b = "1"
# print(bin(int(a,2)+int(b,2)))

#70
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==1:
#             return 1
#         elif n==2:
#             return 2
#         else:
#             return self.climbStairs(n-1)+self.climbStairs(n-2)
# test = Solution()
# print(test.climbStairs(3))
# import Levenshtein
# word1 = "horse"
# word2 = "ros"
# print(Levenshtein.distance(word1,word2))
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if '{}' in s or '()' in s or '[]' in s:
#             s=s.replace('{}','')
#             s=s.replace('()','')
#             s=s.replace('[]','')
#         return s==''
# test = Solution()
# s = "()"
# print(test.isValid(s))
nums = [1,1,2]
nums = list(set(nums))
print(nums)
