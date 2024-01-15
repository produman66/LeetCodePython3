class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapp = dict()
        mapp1 = dict()

        for i in range(len(s)):
            mapp[s[i]] = mapp.get(s[i], 0) + 1
            mapp1[t[i]] = mapp1.get(t[i], 0) + 1

        return mapp == mapp1


sol = Solution()
sl = "car"
sl1 = "rat"

print(sol.isAnagram(sl, sl1))
