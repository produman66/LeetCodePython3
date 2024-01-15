from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i in range(len(nums)):
            if nums[i] not in set1:
                set1.add(nums[i])
            else:
                return True
        return False


sol = Solution()

nums = [1, 2, 3, 4]
nums1 = [2, 2, 3, 1]

ans = sol.containsDuplicate(nums)
ans1 = sol.containsDuplicate(nums1)

print(ans)
print(ans1)
