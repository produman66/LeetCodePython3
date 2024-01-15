class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        sett = set()

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if s[i] in map and map[s[i]] != t[i]: return False
            elif s[i] not in map and t[i] in sett: return False
            elif s[i] not in map:
                map[s[i]] = t[i]
                sett.add(t[i])

        return True

sol = Solution()
s = "badc"
t = "baba"

print(sol.isIsomorphic(s, t))

