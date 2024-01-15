from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        ans = []
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            t = target - nums[i]

            if (t in d and d[t] != i):
                ans.append(i)
                ans.append(d[t])
                return ans

        return ans

sol = Solution()
sl = [3, 2, 4]
asn = sol.twoSum(sl, 6)

for i in asn:
    print(i)