class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contains_seen = {}
        for i,value in enumerate(nums):
            if value in contains_seen and i - contains_seen[value] <=k:
                return True
            else:
                contains_seen[value] = i
        return False           