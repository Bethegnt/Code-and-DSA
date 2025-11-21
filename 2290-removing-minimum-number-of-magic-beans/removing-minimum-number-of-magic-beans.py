class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        total = sum(beans)
        ans = total
        for i,b in enumerate(beans):
            keep = b*(n-i)
            removed = total - keep
            if removed < ans:
                ans = removed
        return ans