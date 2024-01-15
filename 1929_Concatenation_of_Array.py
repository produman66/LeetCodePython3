from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for j in range(len(nums) * 2):
            ans.append(nums[j % len(nums)])
        return ans

sol = Solution()
a = [1, 2, 3]



print(sol.getConcatenation(a))