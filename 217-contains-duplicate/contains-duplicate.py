class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()
        for i in nums:
            if i in duplicate_set:
                return True
            duplicate_set.add(i)
        return False        
        