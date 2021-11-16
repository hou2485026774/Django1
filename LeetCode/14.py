from typing import List


class Solution:
    def longestCommonPrefix(self, strs):
        res = ''
        for i in zip(*strs):
            print(i)
            if len(set(i))==1:
                res+=i[0]
            else:
                break
        return res

test1 = Solution()
strs = ["flower","flow","flight"]
print(test1.longestCommonPrefix(strs))
