from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        ans.append(-1)
        max = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            ans.insert(0, max)
            if (arr[i] > max): max = arr[i]
        return ans


sol = Solution()
a = [17,18,5,4,6,1]



asn = sol.replaceElements(a)

for i in asn:
    print(i)