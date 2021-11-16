from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j)<=k and nums[i]==nums[j]:
                    return True
                else:
                    return False
nums = [1,2,3,1,2,3]
k = 2
test = Solution()
print(test.containsNearbyDuplicate(nums,k))


