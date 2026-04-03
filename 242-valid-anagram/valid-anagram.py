class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts, countT = {}, {}

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for c in counts:
            if counts[c] != countT.get(c, 0):
                return False

        return True