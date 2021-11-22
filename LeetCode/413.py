import random
from typing import List

# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         #计算相邻两个数的差值
#
#         diffs = []
#         for i in range(len(nums) - 1):
#             diffs.append(nums[i + 1] - nums[i])
#         # 第二次遍历
#         cons = []
#         a = 1
#         for i in range(1, len(diffs)):
#             if diffs[i] == diffs[i - 1]:
#                 a += 1
#             else:
#                 cons.append(a)
#                 a = 1
#         cons.append(a)
#         # 第三次遍历
#         res = 0
#         for num in cons:
#             res += int(self.calc(num))
#         return res
#         # 用于计算cons内每个数代表的等差数列个数
#
#     def calc(self, n):
#         if n == 1:
#             return 0
#         n += 1
#         return (n - 2) * (n - 1) / 2
#
# test = Solution()
# nums = [1,5,3,4]
# print(test.numberOfArithmeticSlices(nums))
#
#
# nums.sort()
# print(nums)
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         nums = list(set(nums))
#         nums.sort()
#         if len(nums)<=2:
#             return nums[-1]
#         else:
#             return nums[-3]
# nums = [2,2,3,1]
# test = Solution()
# print(test.thirdMax(nums))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = []
        if sum(nums)%2!=0:
            return False
        for i in nums:
            if sum(res)==sum(nums)/2:
                break
            else:
                res.append(i)
        return True
test = Solution()
nums = [1,2,3,5]
print(test.canPartition(nums))
