from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target, left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                left_result = findFirst(nums, target, left, mid - 1)
                return mid if left_result == -1 else left_result
            elif nums[mid] < target:
                return findFirst(nums, target, mid + 1, right)
            else:
                return findFirst(nums, target, left, mid - 1)
        
        def findLast(nums, target, left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                right_result = findLast(nums, target, mid + 1, right)
                return mid if right_result == -1 else right_result
            elif nums[mid] < target:
                return findLast(nums, target, mid + 1, right)
            else:
                return findLast(nums, target, left, mid - 1)
        if not nums:
            return [-1, -1]
        first = findFirst(nums, target, 0, len(nums) - 1)
        last = findLast(nums, target, 0, len(nums) - 1)
        return [first, last]