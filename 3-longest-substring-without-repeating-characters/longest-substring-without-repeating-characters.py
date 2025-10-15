class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        iterate = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in iterate:
                iterate.remove(s[left])
                left +=1
            iterate.add(s[right])
            res = max(res,right - left + 1)
        return res    

        